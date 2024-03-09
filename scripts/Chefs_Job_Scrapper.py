from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient
import csv
from datetime import datetime

def extract_text(element):
    return element.text.strip() if element else None

# Set up the Selenium webdriver (make sure you have the appropriate webdriver for your browser)
driver = webdriver.Chrome()

# Replace 'your_url_here' with the URL of the page containing the job posting
url = 'https://bikroy.com/en/ads/bangladesh/chef-jobs'
driver.get(url)

# Wait for the page to load (you may need to adjust the waiting time)
driver.implicitly_wait(40)

# Get the page source after it has loaded
page_source = driver.page_source

# Close the browser window
driver.quit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all job postings on the page
job_postings = soup.find_all('div', class_='content--3JNQz')

# Create a list to store the extracted data
data_list = []

for job_posting in job_postings:
    title = extract_text(job_posting.find('h2', class_='heading--2eONR'))

    # Extract the owner name
    owner_name = extract_text(job_posting.find('div').find_next('div'))

    # Check if salary_range_element contains span elements
    salary_range_element = job_posting.find('div', class_='price--3SnqI')
    salary_range_spans = salary_range_element.find_all('span') if salary_range_element else None
    salary_range = extract_text(salary_range_spans[0]) if salary_range_spans else "Not found"

    location_and_job = extract_text(job_posting.find('div', class_='description--2-ez3'))
    job_posting_date = extract_text(job_posting.find('div', class_='updated-time--1DbCk'))

    # Split the location and job using a comma
    location, job = location_and_job.split(', ') if location_and_job else (None, None)

    # Append the data to the list
    data_list.append({
        'title': title,
        'owner_name': owner_name,
        'salary_range': salary_range,
        'location': location,
        'job': job,
        'job_posting_date': job_posting_date,
        'timestamp': datetime.now()
    })

# Connect to MongoDB
client = MongoClient('localhost', 27017)
database = client['local']
collection = database['Data_from_BikroyJobs_website']

# Insert data into MongoDB
collection.insert_many(data_list)

print(f"Data has been successfully saved to MongoDB")
