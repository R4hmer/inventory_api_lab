# Inventory Management System (Flask + CLI)

## Overview

This is a simple inventory management system built using Flask. It allows users to manage products through a REST API and a CLI tool. The project also integrates the OpenFoodFacts API to fetch real product data.

## Features

- Create inventory items
- View all items
- View a single item
- Update items
- Delete items
- Search products using OpenFoodFacts API
- CLI interface for interacting with the API
- Automated tests using pytest

## Technologies Used

- Python
- Flask
- Requests
- Pytest
- OpenFoodFacts API


## Project Setup

### 1. Clone the project

git clone 
cd inventory_api_lab

### 2. Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install flask requests pytest

### 3. Running the application
python app.py


## Running CLI 
python cli.py

