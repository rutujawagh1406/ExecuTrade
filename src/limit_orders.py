import json, uuid, time, logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(message)s'
)

def _write_log(record: dict):
    logging.info(json.dumps(record))

def place_limit_order(symbol: str, side: str, quantity: float, price: float):
    """Simulate a Binance Futures LIMIT order."""
    order = {
        "order_id": str(uuid.uuid4()),
        "timestamp": int(time.time() * 1000),
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "status": "NEW"
    }
    _write_log(order)
    print(f"✅ MOCK Limit Order Accepted: {order}")
