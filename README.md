# Exam-For-Data-Engineer-Position

## Problem Statement
The task involves the construction of two Airflow Directed Acyclic Graphs (DAGs) to facilitate the scraping of data from distinct websites and subsequently uploading the gathered information into a local MongoDB database. The specifics of each DAG are outlined below:

DAG-1:

The objective is to collect data from two sources:

1. Source-1: Utilize the [website](https://www.scrapethissite.com/pages/simple/) to extract information on countries, encompassing details such as capital, population, and area. The retrieved data is to be saved in a CSV file. The order of scraping is left to the implementer's discretion. The DAG is scheduled to run weekly on Sundays at 12 AM.

2. Source-2: Then use another [website](https://www.scrapethissite.com/pages/forms/) to extract data spanning multiple pages. Save the collected information in a CSV file, followed by uploading the file to MongoDB. The choice of Database and Collection names is up to the implementer.

DAG-2:

The primary goal is to retrieve job postings for "chef-jobs" from Bikroy.com using Selenium for the extraction process. The process is divided into three steps:

1. Step - 1: Visit Bikroy.com and select the "Jobs" category.
2. Step - 2: Choose the "Chef" subcategory.
3. Step - 3: Extract all the job posting details available on this page.
Upon successful scraping, store the data in a tabular (CSV) format, and upload the file to MongoDB. This DAG is scheduled to execute on the first day of each month at 12 AM.

