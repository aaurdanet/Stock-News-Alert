import requests
import smtplib

STOCK = "TSLA" #stock to query
COMPANY_NAME = "Tesla Inc" #news about to query
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "" #insert your stock API key
NEWS_API_KEY = "" #insert your news API key

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "language": "en",
    "apikey": NEWS_API_KEY,

}


def percentage_change(todays_price, yesterdays_price):
    up = "🔺"
    down = "🔻"
    difference = todays_price - yesterdays_price
    percentage = abs((difference / yesterdays_price) * 100)
    if difference < 0:
        result = [percentage, down]
        return result
    else:
        result = [percentage, up]
        return result


stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
print(stock_response.raise_for_status())
stock_data = stock_response.json()

list_of_days = list(stock_data['Time Series (Daily)'])

today_date = list_of_days[0]
yesterday_date = list_of_days[1]

today_price = float(stock_data['Time Series (Daily)'][today_date]["4. close"])
yesterday_price = float(stock_data['Time Series (Daily)'][yesterday_date]["4. close"])

percent = percentage_change(today_price, yesterday_price)

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
print(news_response.raise_for_status())
news_data = news_response.json()

articles = news_data["articles"][0:3]

article_1 = [articles[0]["title"], articles[0]["description"], articles[0]["url"]]
article_2 = [articles[1]["title"], articles[1]["description"], articles[1]["url"]]
article_3 = [articles[2]["title"], articles[2]["description"], articles[2]["url"]]


def remove_link(description):

    if description is None:
        description = "Not available from this source."
        return description
    
    link_index = description.find("https://")
    if link_index != -1:
        return description[:link_index]
    else:
        return description


article_1[1] = remove_link(article_1[1])
article_2[1] = remove_link(article_2[1])
article_3[1] = remove_link(article_3[1])

if percent[0] >= 1:
    msg = (
    f"Subject: {STOCK}: {percent[1]}{percent[0]:.2f}%\n\n"
    f"News Report\n\n"
    f"Headline: {article_1[0]}\nBrief: {article_1[1]}\nLink to page: {article_1[2]}\n\n"
    f"Headline: {article_2[0]}\nBrief: {article_2[1]}\nLink to page: {article_2[2]}\n\n"
    f"Headline: {article_3[0]}\nBrief: {article_3[1]}\nLink to page: {article_3[2]}\n\n"
)
    msg_encoded = msg.encode('utf-8')
    my_email = "" #insert senders email
    my_password = "" #insert email app password
    connection = smtplib.SMTP("smtp.gmail.com") #insert senders smtp service Ex. Yahoo, Gmail, Outlook...
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="", #insert destination address 
                        msg=msg_encoded)
    print(msg)
