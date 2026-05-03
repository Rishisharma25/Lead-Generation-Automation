# Lead Generation Automation

## Overview

This project implements a simple lead generation pipeline using a company dataset from Kaggle. It extracts relevant business information, performs data cleaning, and generates structured leads suitable for outreach or analysis.

The original dataset is large (~1GB) and sourced from Kaggle. A smaller sample dataset (50 records) is included in this repository for demonstration and testing purposes.


## Dataset

Source: Kaggle Companies Dataset
The dataset contains company-level information such as name, domain, LinkedIn URL, location, industry, and company size.

## Features

* Data extraction and column selection
* Data cleaning (removal of duplicates and handling missing values)
* Email generation using company domain (e.g., [contact@domain.com](mailto:contact@domain.com))
* Website generation from domain
* Export of structured leads to Excel

## Output

The script generates an Excel file containing 20–30 cleaned lead entries with the following fields:

* Name
* Generated Email
* Website
* LinkedIn
* City
* Country
* Industry
* Company Size

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Place the dataset file (companies.csv) in the project directory

3. Run the script:
   python lead_gen_automation.py

## Assumptions

* Email addresses are generated using standard company patterns and may not represent actual contact emails.
* Website URLs are derived from available domain data.
* Only a subset of records is used to meet assignment requirements.

## Technologies Used

* Python
* Pandas
* OpenPyXL

## Conclusion

This project demonstrates practical data processing and automation skills, including handling incomplete datasets and transforming raw data into usable business leads.
