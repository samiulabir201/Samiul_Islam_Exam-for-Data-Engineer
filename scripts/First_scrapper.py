from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import csv
import pandas as pd

# Set up the webdriver (replace 'path_to_chromedriver' with the path to your chromedriver executable)
driver = webdriver.Chrome()

# URL of the website containing the data
url = 'https://www.scrapethissite.com/pages/simple/'  # Replace with the actual URL

# Set a timer to allow the website to load (adjust the sleep duration as needed)
driver.get(url)

# Explicitly wait for elements to be present on the page
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

# Function to scrape data and save to CSV
def scrape_and_save_to_csv():
    # Wait for the elements to be present
    countries = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'country-name')))
    capitals = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'country-capital')))
    populations = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'country-population')))
    areas = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'country-area')))

    data = []
    for i in range(len(countries)):
        country = countries[i].text
        capital = capitals[i].text
        population = populations[i].text
        area = areas[i].text

        data.append([country, capital, population, area])

    # Save data to CSV
    csv_file_path = 'countries_data.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Country', 'Capital', 'Population', 'Area'])
        csv_writer.writerows(data)

    return csv_file_path

# Call the function to scrape and save data
csv_file_path = scrape_and_save_to_csv()

# Close the webdriver
driver.quit()

# Upload data to MongoDB
client = MongoClient('localhost', 27017)
database = client['local']
collection = database['Data_from_First_scrapped_website']

# Read CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert DataFrame to a list of dictionaries for MongoDB insertion
data_for_mongo = df.to_dict(orient='records')

# Insert data into MongoDB
collection.insert_many(data_for_mongo)

print(f'Data has been successfully uploaded to MongoDB in the "local" database, "Data_from_First_scrapped_website" collection.')
