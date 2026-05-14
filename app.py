from flask import Flask, request
from binance.client import Client

app = Flask(__name__)

api_key = "7QnnBFIApGdHy02NhsEoTannv4xsV8NlOSPky8pdd6oPmgVFDJcol7z1vipybVVd"
api_secret = "Cid8qbL9It4x9IgumELttVjTKGD1ypP1MTt7HuUWJBiFYmpbYqaUZLHSRukNWMaD"

client = Client(
    api_key,
    api_secret,
    testnet=True
)

client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    side = data['side']

    if side == "BUY":

        client.futures_create_order(
            symbol='BTCUSDT',
            side='BUY',
            type='MARKET',
            quantity=0.001
        )

    if side == "SELL":

        client.futures_create_order(
            symbol='BTCUSDT',
            side='SELL',
            type='MARKET',
            quantity=0.001
        )

    return "ok"

@app.route('/')
def home():
    return "BOT RUNNING"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
