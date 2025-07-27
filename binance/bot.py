from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        self.logger = logging.getLogger(__name__)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_params = {
                "symbol": symbol,
                "side": SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == ORDER_TYPE_LIMIT:
                if price is None:
                    raise ValueError("Limit orders require a price.")
                order_params.update({
                    "price": price,
                    "timeInForce": TIME_IN_FORCE_GTC
                })

            order = self.client.futures_create_order(**order_params)
            self.logger.info(f"Order placed: {order}")
            return order

        except Exception as e:
            self.logger.error(f"Error placing order: {str(e)}")
            return None
