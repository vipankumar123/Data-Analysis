# Django Data Visualization Project

This Django web application allows users to upload CSV files, perform data analysis using pandas and numpy, and visualize the results using matplotlib and seaborn.

## Features

- **File Upload**: Users can upload CSV files containing organizational data.
- **Data Analysis**: Performs basic data analysis including displaying data head, summary statistics, and identifying missing values.
- **Data Visualization**: Generates histograms for numerical columns using matplotlib and seaborn.
- **User Interface**: Provides a simple web interface to interact with uploaded data and view analysis results.

## Requirements

- Python 3.x
- Django
- pandas
- numpy
- matplotlib
- seaborn

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>

## Create a virtual environment:

python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`

## Install dependencies:

pip install -r requirements.txt

## Apply migrations:

python manage.py migrate

## Collect static files:

python manage.py collectstatic

## Run the Django development server:

python manage.py runserver

## Access the application:

Open your web browser and go to http://localhost:8000 to access the application.

## Usage

Upload CSV File:

Click on the "Upload CSV File" button on the home page.
Select a CSV file and click on the "Upload" button.

## View Analysis Results:

After uploading, you will be redirected to a page displaying data analysis results.
The results include data head, summary statistics, missing values, and histograms for numerical columns.

## Explore Visualizations:

Scroll down to view the histograms generated for each numerical column.
Each histogram provides insights into the distribution of data within that column.

## Sample Graphs

Histograms

Founded Year Distribution

Number of Employees Distribution