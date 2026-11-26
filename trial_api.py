import os
import sys
import requests
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

API_KEY = os.getenv("RESTCOUNTRIES_API_KEY")
URL = "https://api.restcountries.com/countries/v5"


def fetch_country(name):
    """Return the first matching country as a dictionary, or None."""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get(URL, params={"q": name}, headers=headers, timeout=(10, 30))
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Could not fetch data: {error}")
        return None

    countries = response.json().get("data", {}).get("objects", [])
    return countries[0] if countries else None


def print_summary(country):
    """Print a readable summary of one country."""
    name = country["names"]["common"]
    capitals = country.get("capitals", [])
    capital = capitals[0]["name"] if capitals else "N/A"
    currencies = country.get("currencies", [])
    currency = f'{currencies[0]["name"]} ({currencies[0]["code"]})' if currencies else "N/A"
    languages = ", ".join(lang["name"] for lang in country.get("languages", []))
    population = country.get("population", 0)
    area = country.get("area", {}).get("kilometers", 0)

    print("=" * 40)
    print(f"  COUNTRY SUMMARY: {name.upper()}")
    print("=" * 40)
    print(f"{'Capital:':<14}{capital}")
    print(f"{'Region:':<14}{country.get('region', 'N/A')}")
    print(f"{'Population:':<14}{population:,} people")
    print(f"{'Area:':<14}{area:,.0f} km²")
    print(f"{'Currency:':<14}{currency}")
    print(f"{'Languages:':<14}{languages or 'N/A'}")
    print("=" * 40)


if __name__ == "__main__":
    country = fetch_country(input("Enter a country: "))
    if country:
        print_summary(country)
    else:
        print("No data found.")