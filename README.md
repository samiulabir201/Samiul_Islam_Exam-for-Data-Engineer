# Exam-For-Data-Engineer-Position

## Problem Statement
The task involves the construction of two Airflow Directed Acyclic Graphs (DAGs) to facilitate the scraping of data from distinct websites and subsequently uploading the gathered information into a local MongoDB database. The specifics of each DAG are outlined below:

DAG-1:

The objective is to collect data from two sources:

1. Source-1: Utilize the [website](https://www.scrapethissite.com/pages/simple/) to extract information on countries, encompassing details such as capital, population, and area. The retrieved data is to be saved in a CSV file. The order of scraping is left to the implementer's discretion. The DAG is scheduled to run weekly on Sundays at 12 AM.

2. Source-2: Then use another [website](https://www.scrapethissite.com/pages/forms/) to extract data spanning multiple pages. Save the collected information in a CSV file, followed by uploading the file to MongoDB. The choice of Database and Collection names is up to the implementer.

DAG-2:

The primary goal is to retrieve job postings for "chef-jobs" from Bikroy.com using Selenium for the extraction process. The process is divided into three steps:

1. Step - 1: Visit [Bikroy.com](https://bikroy.com/en/ads/bangladesh/chef-jobs) and select the "Jobs" category.
2. Step - 2: Choose the "Chef" subcategory.
3. Step - 3: Extract all the job posting details available on this page.
Upon successful scraping, store the data in a tabular (CSV) format, and upload the file to MongoDB. This DAG is scheduled to execute on the first day of each month at 12 AM.

## Prerequisites:
1. Ensure that Docker is installed on your machine.
2. Have Python and pip installed for managing Python packages.

## Building and Running the project:
1. Step 1: Clone the project repository into your desired directory.
```
  git clone https://github.com/samiulabir201/Samiul_Islam_Exam-for-Data-Engineer /path/to/your/project
  cd /path/to/your/project

```
2. Step 2: Set Up Airflow DAGs and Build Docker Image
   Install apache airflow using the command:
   ```
      pip install apache-airflow
   ```
   Run the following commands sequentially:

   2.1
   ```
     curl 'https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml' -o 'docker-compose.yaml'
   ```
   2.2 
   ```
     docker compose up airflow-init
   ```
   2.3
   ```
     docker compose up
   ```
3. Step 3: Update Airflow Connections for MongoDB

    3.1 Access Airflow Web UI:
        Open localhost:8080 in your browser.

    3.2 Configure Connections:

              Go to Admin -> Connections and add a new connection for MongoDB.
              Conn Id: mongo_conn_id
              Conn Type: MongoDB
              Host: mongo
              Port: 27017
              Schema: Your MongoDB database name
              Login: Your MongoDB username
              Password: Your MongoDB password

5. Step 4: Run Airflow DAGs

Trigger DAGs:
In the Airflow Web UI, locate the DAGs (with DAG Id= DAG_1 and DAG Id= chef_jobs_extraction) and trigger them manually or wait for the scheduled runs.

5. Step 5: Monitor Execution

Check Logs:

Monitor the execution logs through the Airflow Web UI.
Verify MongoDB:

Connect to your MongoDB instance and check if the scraped data has been successfully stored.


