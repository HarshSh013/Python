import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
Stock_API_key="ODA56JC3RZO0CAD4"
News_API_key="c506446b63544028b668c47329f5193a"


account_sid = "ACee72c4a3c7b75936ceabdb63da7ed69f"
auth_token = "b1d9d1b02f42d8d22d534e83d237f2d3"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":Stock_API_key,
}

response=requests.get(STOCK_ENDPOINT,stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)
#TODO 2. - Get the day before yesterday's closing stock price
daybefore_yesterday_data=data_list[1]
daybefore_yesterday_closing_price=daybefore_yesterday_data["4. close"]
print(daybefore_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=float(yesterday_closing_price)-float(daybefore_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_perc=(difference/float(yesterday_closing_price)) * 100
print(diff_perc)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if (diff_perc > 1):
#     print("getnews")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if (abs(diff_perc) > 1):
    news_params={
        "apiKey":News_API_key,
        "qInTitle":COMPANY_NAME,
    }
    news_reponse=requests.get(NEWS_ENDPOINT,news_params)
    articles=news_reponse.json()["articles"]
    three_articles=articles[:3]
    print(three_articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
formatted_articles=[f"{STOCK_NAME}: {up_down}{diff_perc}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
client = Client(account_sid, auth_token)


#TODO 9. - Send each article as a separate message via Twilio. 
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+18788812643',
        to='+917073396759'
    )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

