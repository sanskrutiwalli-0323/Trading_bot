import logging

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        logging.info(f"Placing order: {symbol}, {side}, {order_type}, {quantity}, {price}, {stop_price}")

        try:
            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            elif order_type == "STOP_LIMIT":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP",
                    quantity=quantity,
                    price=price,
                    stopPrice=stop_price,
                    timeInForce="GTC"
                )

            logging.info(f"Order Response: {response}")
            return response

        except Exception as e:
            logging.error(f"Order failed: {e}")
            raise
