import json, uuid, time, logging


logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(message)s'
)

def _write_log(record: dict):
    logging.info(json.dumps(record))

def place_market_order(symbol: str, side: str, quantity: float):
    """Simulate a Binance Futures MARKET order."""
    order = {
        "order_id": str(uuid.uuid4()),
        "timestamp": int(time.time() * 1000),
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "MARKET",
        "quantity": quantity,
        "status": "FILLED",
        "price": "MARKET"
    }
    _write_log(order)
    print(f"✅ MOCK Market Order Filled: {order}")
