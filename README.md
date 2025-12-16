# Quant Market Dashboard

## Overview
This project is a Python-based quantitative dashboard that ingests market tick data,
processes analytics, and visualizes insights using an interactive web interface.

## Features
- Market data ingestion from CSV
- Analytical computations on tick data
- Interactive dashboard for visualization
- Modular and scalable architecture

## Project Structure
- app.py → Main application entry point
- data_ingestion.py → Data loading & preprocessing
- analytics.py → Market analytics logic
- storage.py → Data storage handling
- ticks.csv → Sample input data
- requirements.txt → Dependencies

## Tech Stack
- Python
- Pandas
- Streamlit
- Plotly

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`
2. Run the application  
   `streamlit run app.py`

## Use Case
Designed for quantitative analysis and dashboard-based visualization of financial data.
