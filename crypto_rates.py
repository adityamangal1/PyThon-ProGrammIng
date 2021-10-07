import requests
import json

curr = input("\nWhich crypto currency rate you want to know? ")
crypto=["BTC","LTC","ETH","ETC","DOGE"]

if curr.upper() in crypto:
    if curr.upper() == "DOGE":
        response = requests.get("https://coinremitter.com/api/v2/get-coin-rate")
        data = response.json()
        currency = data["data"]["DOGE"]["symbol"]
        price = data["data"]["DOGE"]["price"]

    else:
        response = requests.get("https://api.coinbase.com/v2/prices/" + curr + "-USD/spot")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]

print(f"1 {currency}\nRate = ${price}")
