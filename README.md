Here's a quick example of what your `README.md` file could look like:

```markdown
# Country Data Fetcher

This Python script fetches country data from the [Rest Countries API](https://restcountries.com/) and formats it into a JSON file. The JSON file contains information about each country's code, Arabic name, and key (concatenation of IDD root and suffixes).

## Usage

1. Install the required packages using pip:

   ```bash
   pip install requests
   ```

2. Run the script `fetch_countries.py`:

   ```bash
   python fetch_countries.py
   ```

3. The script will fetch the country data and save it to a file named `countries.json` in the same directory.

## File Structure

- `fetch_countries.py`: Python script to fetch and format country data.
- `countries.json`: Output JSON file containing country data.

## Data Format

The JSON data is formatted as follows:

```json
[
    {
        "code": "AE",
        "name": "الإمارات العربية المتحدة",
        "key": "+971"
    },
    {
        "code": "SA",
        "name": "المملكة العربية السعودية",
        "key": "+966"
    },
    ...
]
```

Each entry contains the country code (`code`), Arabic name (`name`), and key (`key`), which is a concatenation of IDD root and suffixes.

## Dependencies

- Python 2.7+
- requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to adjust the content and structure of the `README.md` file to fit your project's needs.
