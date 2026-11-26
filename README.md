# Country Summary

A small Python script that fetches live data about a country from the [REST Countries API](https://restcountries.com) and prints a clean, human-readable summary: no JSON in sight.

## What it shows

- Capital
- Region
- Population (formatted with thousands separators)
- Area in km²
- Currency
- Languages

## Requirements

- Python 3.8 or newer
- A free API key from [restcountries.com](https://restcountries.com/sign-up)

## Setup

1. Clone the repository and open the project folder.

2. Install the dependencies:

   ```
   pip install requests python-dotenv
   ```

3. Create a file named `.env` in the project folder and add your key (no quotes, no spaces around `=`):

   ```
   RESTCOUNTRIES_API_KEY=your_key_here
   ```

   The `.env` file is listed in `.gitignore`, so your key is never uploaded.

## Usage

```
python trial_api.py
```

Type a country name when prompted, for example `Kenya`.

## Example output

```
========================================
  COUNTRY SUMMARY: KENYA
========================================
Capital:      Nairobi
Region:       Africa
Population:   54,227,015 people
Area:         580,367 km²
Currency:     Kenyan shilling (KES)
Languages:    English, Swahili
========================================
```

## How it works

- `fetch_country()` sends a request to the API, retries if the server is slow, and returns the matching country (or `None` if nothing is found).
- `print_summary()` picks out the useful fields and prints them with labels and formatted numbers.
- Errors such as a missing key, a timeout or an unknown country produce a friendly message instead of a crash.

## Notes
- The free plan has a monthly request limit, so avoid running the script in a loop.

## Credits

Data provided by [REST Countries](https://restcountries.com).
