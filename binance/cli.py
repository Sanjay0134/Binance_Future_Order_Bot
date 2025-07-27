from bot import BasicBot
from config import API_KEY, API_SECRET
from utils import setup_logger, validate_order_input

def main():
    setup_logger()
    bot = BasicBot(API_KEY, API_SECRET, testnet=True)

    print("Welcome to Binance Futures Testnet Trading Bot\n")

    symbol = input("Enter trading pair (e.g. BTCUSDT): ").strip()
    side = input("Enter order side (buy/sell): ").strip().lower()
    order_type = input("Enter order type (MARKET/LIMIT): ").strip().upper()
    quantity = float(input("Enter quantity: "))
    price = None

    if order_type == "LIMIT":
        price = float(input("Enter limit price: "))

    try:
        validate_order_input(symbol, side, order_type, quantity, price)
        response = bot.place_order(symbol, side, order_type, quantity, price)
        if response:
            print("✅ Order placed successfully!")
            print(response)
        else:
            print("❌ Order failed. Check logs for details.")

    except Exception as e:
        print(f"Input Error: {str(e)}")

if __name__ == "__main__":
    main()
