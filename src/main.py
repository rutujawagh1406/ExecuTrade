import sys
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.oco import place_oco_order
from advanced.twap import place_twap_order

def main():
    if len(sys.argv) < 5:
        print("""Usage:
  Market Order: python main.py market SYMBOL SIDE QUANTITY
  Limit Order : python main.py limit SYMBOL SIDE QUANTITY PRICE
  OCO Order   : python main.py oco SYMBOL SIDE QTY TP_PRICE STOP_PRICE STOP_LIMIT_PRICE
  TWAP Order  : python main.py twap SYMBOL SIDE TOTAL_QTY [SLICES] [INTERVAL_SEC]
""")
        return

    order_type = sys.argv[1].lower()
    symbol = sys.argv[2].upper()
    side = sys.argv[3].upper()
    quantity = float(sys.argv[4])

    if order_type == 'market':
        place_market_order(symbol, side, quantity)

    elif order_type == 'limit':
        if len(sys.argv) < 6:
            print("❌ Price is required for limit orders.")
            return
        price = float(sys.argv[5])
        place_limit_order(symbol, side, quantity, price)

    elif order_type == 'oco':
        if len(sys.argv) < 8:
            print("❌ Usage: python main.py oco SYMBOL SIDE QTY TP_PRICE STOP_PRICE STOP_LIMIT_PRICE")
            return
        take_profit = float(sys.argv[5])
        stop_price = float(sys.argv[6])
        stop_limit_price = float(sys.argv[7])
        place_oco_order(symbol, side, quantity, take_profit, stop_price, stop_limit_price)

    elif order_type == 'twap':
        slices = int(sys.argv[5]) if len(sys.argv) > 5 else 4
        interval = int(sys.argv[6]) if len(sys.argv) > 6 else 5
        place_twap_order(symbol, side, quantity, slices, interval)

    else:
        print("❌ Invalid order type. Use 'market', 'limit', 'oco', or 'twap'.")

if __name__ == "__main__":
    main()
