# Amazon-API

This repository contains a Python script that interacts with the Amazon API to fetch real-time data on deals and promotions. The script sends HTTP requests, processes JSON responses, and saves relevant data to a local file.

## Features

- Fetches real-time data on Amazon deals using the RapidAPI Amazon API.
- Filters deals by country, category, price range, and star rating.
- Handles JSON decoding errors gracefully.
- Saves the retrieved data in a formatted JSON file for further analysis.

## Requirements

- Python 3.7 or higher
- A valid RapidAPI key to access the Amazon API

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/fhaelmarinho/Amazon-API.git
   cd Amazon-API
    ```
2. Install the required Python packages::
   ```bash
   pip install requests
   ```
3. Configure your API credentials:

Create a file named ```headers.py``` in the project directory.
Add the following variables to the file:

 ```bash
   key = "your-rapidapi-key"
   host = "real-time-amazon-data.p.rapidapi.com"
   ```

## Usage

1. Run the script:
```bash
python main.py
```
2. The script will fetch data from the Amazon API and save it to a file named ```amazon_data.json``` in the project directory.

## File Structure

```bash
Amazon-API/
├── [main.py](http://_vscodecontentref_/1)          # Main script to fetch and process data
├── [headers.py](http://_vscodecontentref_/2)       # API credentials (not included in the repository)
├── [amazon_data.json](http://_vscodecontentref_/3) # Output file with fetched data (generated after running the script)
├── [README.md](http://_vscodecontentref_/4)        # Project documentation
```

## Notes

Ensure you have a valid RapidAPI key to access the Amazon API.
The script currently fetches deals for the US market and the "electronics" category. You can modify the querystring variable in main.py to customize the filters.

## License
This project is licensed under the MIT License. See the LICENSE file for details.