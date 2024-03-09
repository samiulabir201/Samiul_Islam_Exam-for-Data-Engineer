import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient

# Function to scrape data from a single page
def scrape_page(driver, page_num):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={page_num}&per_page=100"
    driver.get(url)
    
    time.sleep(30)  # Wait for 30 seconds to load the webpage

    data = []
    teams = driver.find_elements(By.CLASS_NAME, 'team')
    for team in teams:
        team_data = {}
        team_data['Team Name'] = team.find_element(By.CLASS_NAME, 'name').text.strip()
        team_data['Year'] = team.find_element(By.CLASS_NAME, 'year').text.strip()
        team_data['Wins'] = team.find_element(By.CLASS_NAME, 'wins').text.strip()
        team_data['Losses'] = team.find_element(By.CLASS_NAME, 'losses').text.strip()
        team_data['OT Losses'] = team.find_element(By.CLASS_NAME, 'ot-losses').text.strip()
        team_data['Win%'] = team.find_element(By.CLASS_NAME, 'pct').text.strip()
        team_data['Goals For (GF)'] = team.find_element(By.CLASS_NAME, 'gf').text.strip()
        team_data['Goals Against (GA)'] = team.find_element(By.CLASS_NAME, 'ga').text.strip()
        team_data['+/-'] = team.find_element(By.CLASS_NAME, 'diff').text.strip()

        data.append(team_data)

    return data

# Set up the webdriver
driver = webdriver.Chrome()

# Scrape data from all 4 pages
all_data = []
for page_num in range(1, 5):
    page_data = scrape_page(driver, page_num)
    all_data.extend(page_data)

# Close the webdriver
driver.quit()

# Save the data to a CSV file
csv_file_path = 'Team Data.csv'
header = ['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win%', 'Goals For (GF)', 'Goals Against (GA)', '+/-']

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(all_data)

# Upload data to MongoDB
client = MongoClient('localhost', 27017)
database = client['local']
collection = database['Data_from_Second_scrapped_website']

# Read CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert DataFrame to a list of dictionaries for MongoDB insertion
data_for_mongo = df.to_dict(orient='records')

# Insert data into MongoDB
collection.insert_many(data_for_mongo)

print(f'Data has been successfully scraped and saved to {csv_file_path}')
