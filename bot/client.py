from binance.client import Client
import time

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        self.client.TIME_OFFSET = -1000  # fixes timestamp issue

    def get_client(self):
        return self.client
