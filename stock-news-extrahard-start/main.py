import smtplib
import requests
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_key = "VQ96U30M1E29LBWG"
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_key
}
alpha_url = "https://www.alphavantage.co/query?"


def get_stock_changes():
    response = requests.get(url=alpha_url, params=alpha_parameters)
    response.raise_for_status()

    daily = response.json()['Time Series (Daily)']
    daily_list = list(daily)  # Converting the response to a list in order to get yesterday's date

    yesterday = daily_list[0]
    day_before_yesterday = daily_list[1]

    yesterday_data = daily[yesterday]
    day_before_yesterday_data = daily[day_before_yesterday]
    print(yesterday_data)
    print(day_before_yesterday_data)

    change = round((float(yesterday_data['4. close']) - float(day_before_yesterday_data['4. close'])) * 100 \
             / float(yesterday_data['1. open']), 2)

    print(change)

    if 2 < change or change < -5:
        get_news(change)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(change):
    news_url = "https://newsapi.org/v2/everything"
    news_api = "849a5cf11e714bf2a33010fbef950f1c"
    news_params = {
        'q': 'tesla',
        'qInTitle' : "title search",
        'language' : 'en',
        'from': '2023 - 10 - 16',
        'sortBy': 'publishedAt',
        'apiKey': news_api
    }

    news = requests.get(url=news_url, params=news_params)
    news.raise_for_status()
    top_three = news.json()['articles'][0:3]

    for news in top_three:
        print(news)

    if change > 2:
        change = True
        send_mail(top_three, change=change)
    elif change < -5:
        change = False
        send_mail(top_three, change=change)


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
my_email = "portopapii@gmail.com"
my_password = "scpg eymd zzqm hybc"
def send_mail(top_three:list, change:bool):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        if change:
            direction = "💹"
        else:
            direction = "🔻"
        connection.login(user=my_email, password=my_password)
        message = f"Subject: TSLA {direction} 5%\n\n"
        for news in top_three:
            message += f"\nHeadline: {news['title']}\nBrief:{news['description']}"
        print(message)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="adjeiboyejnr@gmail.com",
            msg=message.encode()
        )


get_stock_changes()
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
