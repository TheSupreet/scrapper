# Project Scraper and Viewer

This project is a web application for scraping and displaying project details from the HPRERA public dashboard. It includes a Python script for scraping the data and a Flask-based web application to display the details.

## Features

- Scrape project data from the HPRERA public dashboard.
- Display detailed project information on a web interface.
- Responsive and styled HTML/CSS frontend.

## File Structure

project-scraper-viewer/
│
├── app.py # Flask application script
├── project_data.json # JSON file containing scraped project details
├── requirements.txt # List of Python dependencies
├── scrape_projects.py # Python script for scraping project details
│
├── static/
│ └── styles.css # CSS file for styling the HTML
│
└── templates/
  └── index.html # HTML template for displaying project details

## Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt


## Run the Scraper
`python scrape_projects.py`

## Run the Flask Application
`python app.py`


## images:
![op1](https://github.com/user-attachments/assets/f7cdee8c-e278-436e-8430-3b236538251f)
![op2](https://github.com/user-attachments/assets/cade44bb-35e8-457e-9d32-d57fbe2ef736)
