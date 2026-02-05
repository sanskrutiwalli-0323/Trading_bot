import argparse
import logging
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import *
from bot.logging_config import setup_logger

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)
        validate_stop_price(args.stop_price, args.type)

        client = BinanceClient(API_KEY, API_SECRET).get_client()
        order_service = OrderService(client)

        print("\n📤 Order Request:")
        print(vars(args))

        response = order_service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price
        )

        print("\n✅ Order Successful!")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n❌ Order Failed:", str(e))
        logging.error(str(e))

if __name__ == "__main__":
    main()
