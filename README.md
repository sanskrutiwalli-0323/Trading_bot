# Binance Futures Testnet Trading Bot

## Setup

1. Clone repo
2. Create virtual env (optional)
3. Install dependencies:
   pip install -r requirements.txt

4. Add your Binance Testnet API key & secret in cli.py

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000

## Features

- Market & Limit orders
- BUY / SELL support
- Input validation
- Logging to file
- Error handling

## Assumptions

- Binance Futures USDT-M Testnet is used
- User already has testnet balance
