import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()]
    )

def validate_order_input(symbol, side, order_type, quantity, price=None):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs supported")
    if side.lower() not in ("buy", "sell"):
        raise ValueError("Side must be 'buy' or 'sell'")
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Limit orders require a positive price")
