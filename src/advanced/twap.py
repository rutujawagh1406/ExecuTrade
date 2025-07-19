import json, uuid, time, logging, math

logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    format='%(message)s')

def _log(p): logging.info(json.dumps(p))

def place_twap_order(symbol: str,
                     side: str,
                     total_qty: float,
                     slices: int = 4,
                     interval_sec: int = 5):
    slice_qty = total_qty / slices
    twap_id = str(uuid.uuid4())

    for i in range(1, slices + 1):
        payload = {
            "twap_id": twap_id,
            "slice": i,
            "timestamp": int(time.time() * 1000),
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "TWAP",
            "quantity": round(slice_qty, 6),
            "status": "FILLED"
        }
        _log(payload)
        print(f"✅ MOCK TWAP slice {i}/{slices}: {payload}")
        if i < slices:
            time.sleep(interval_sec)   
