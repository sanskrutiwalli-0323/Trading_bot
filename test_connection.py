from binance.client import Client

client = Client("8zGnPrNIX3qWYx2dmnCqx0BSkrfrvPck2YNeslmSf1o9aASEnUUUVVF8QeEJfYWv", "XZwty5Xb2bGbOxPwcOlnXE12YJb503C2MzmkP9NkOLoHnz3q4eNBeyoIbRzhXInM")
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print(client.futures_account())
