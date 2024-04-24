Stock News Alert
Overview

This Python script fetches stock data and news articles related to a specific stock symbol. It calculates the percentage change in the stock price between yesterday and the day before yesterday and sends an email with the news articles if the percentage change is greater than or equal to 1%.
Dependencies

Python 3.x
requests library: Used for making HTTPS requests to fetch stock data and news articles.
smtplib library: Used for sending email notifications.
An internet connection is required to fetch stock data and news articles.

Usage

Ensure you have Python 3.x installed on your system.
Install the required libraries by running:

    pip install requests

Run the main.py script:

    python main.py

Follow the prompts to input your email address and password for sending notifications.
If the percentage change in the stock price is greater than or equal to 1%, you will receive an email with news articles related to the stock.

Configuration

Modify the STOCK variable to specify the stock symbol you're interested in.
Modify the COMPANY_NAME variable to specify the name of the company associated with the stock symbol.
Ensure you have valid API keys for Alpha Vantage (for stock data) and News API (for news articles) and replace the placeholder values in the script with your actual API keys.
