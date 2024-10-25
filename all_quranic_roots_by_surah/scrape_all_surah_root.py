import requests
from bs4 import BeautifulSoup
import json
import re

# Function to scrape data for a given surah number
def scrape_surah(surah_number):
    # Construct the URL
    url = f"https://www.altadabbur.com/quran/suar/roots/{surah_number}"

    # Generate the JSON file name
    json_file_name = f'surah_{str(surah_number).zfill(3)}.json'

    # Send a GET request to fetch the HTML content of the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all tables with the class 'table-roots'
        tables = soup.find_all('table', class_='table-roots')

        # List to store the scraped data
        scraped_data = []

        # Loop through each table and extract the desired information
        for table in tables:
            # Find all rows in the table body
            rows = table.find('tbody').find_all('tr')

            for row in rows:
                # Extract the relevant columns (td elements)
                columns = row.find_all('td')

                # Extract the data from each column
                word = columns[1].text.strip()    # Second column (word in brackets)
                occurrences = columns[2].text.strip()  # Third column (occurrences)

                # Clean the word from brackets
                word_cleaned = word.replace('﴿', '').replace('﴾', '').strip()

                # Convert the occurrences from Arabic to English numbers and strip the "مرة"
                occurrences_cleaned = int(''.join(filter(str.isdigit, occurrences)))

                # Add the extracted data to the list
                scraped_data.append({
                    'root_word': word_cleaned,
                    'occurrences': occurrences_cleaned
                })

        # Sort the scraped data by the Arabic alphabet
        scraped_data = sorted(scraped_data, key=lambda x: x['root_word'])

        # Add the "root_order" field
        for index, item in enumerate(scraped_data):
            item['root_order'] = index + 1

        # Write the scraped data to a JSON file
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json.dump(scraped_data, json_file, ensure_ascii=False, indent=4)

        print(f"Data successfully written to '{json_file_name}'")
    else:
        print(f"Failed to retrieve the webpage for surah {surah_number}. Status code: {response.status_code}")

# Loop through surah numbers from 1 to 114
for surah_number in range(1, 115):
    scrape_surah(surah_number)