import json, uuid, time, logging

logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    format='%(message)s')

def _log(payload: dict):
    logging.info(json.dumps(payload))

def place_oco_order(symbol: str,
                    side: str,
                    quantity: float,
                    take_profit_price: float,
                    stop_price: float,
                    stop_limit_price: float):
    order_id = str(uuid.uuid4())
    payload = {
        "oco_id": order_id,
        "timestamp": int(time.time() * 1000),
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "OCO",
        "quantity": quantity,
        "take_profit_price": take_profit_price,
        "stop_price": stop_price,
        "stop_limit_price": stop_limit_price,
        "status": "NEW"
    }
    _log(payload)
    print(f"✅ MOCK OCO Order Accepted: {payload}")
