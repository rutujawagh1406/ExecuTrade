# ExecuTrade (Mock) – Binance Futures Order Bot

> **Why mock?**  
> Binance Testnet now requires full KYC (Aadhaar) for API keys.  
> To protect personal data while still demonstrating full skills, this bot uses **mock order functions** that generate realistic order objects and structured logs.  
> Swapping to real Binance API later is a two‑line change (see “Going Live” below).

---

## ✨ Features
| Category      | Details                                                        |
| ------------- | -------------------------------------------------------------- |
| Core Orders   | Market & Limit (mandatory)                                     |
| Advanced      | OCO (One‑Cancels‑the‑Other) & TWAP (Time‑Weighted Average Price) |
| Logging       | JSON entries in `bot.log` (order_id, timestamp, symbol, etc.)  |
| Validation    | CLI checks for args, side / symbol upper‑casing, price present |
| Documentation | This README + `report.pdf` with screenshots                    |

---

## 📂 Project Structure
ExecuTrade/
├── bot.log # JSON log file (auto‑generated)
├── README.md # ← You are here
├── report.pdf # Analysis + screenshots (add yours)
└── src/
├── main.py # CLI dispatcher
├── market_orders.py # Mock market logic
├── limit_orders.py # Mock limit logic
└── advanced/
├── oco.py # Mock OCO logic
└── twap.py # Mock TWAP strategy

yaml
Copy
Edit

---

## ⚙️ Installation
```bash
# 1. Clone or unzip the repo
git clone https://github.com/<your-username>/rutuja-binance-bot.git
cd rutuja-binance-bot

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install core deps (no API libraries required for mock)
pip install python-dotenv
Going Live (optional)

nginx
Copy
Edit
pip install python-binance
Then replace the mock dictionaries in market_orders.py and limit_orders.py with client.futures_create_order(...), add .env with API keys, and you are production‑ready.

🚀 Usage
1. Market Order
bash
Copy
Edit
python src/main.py market BTCUSDT BUY 0.01
2. Limit Order
bash
Copy
Edit
python src/main.py limit BTCUSDT SELL 0.01 30000
3. OCO Order (Advanced)
bash
Copy
Edit
python src/main.py oco BTCUSDT SELL 0.01 31000 29500 29480
#        └───┬── └─────┬── └────┬─ TP  └─ Stop └─ Stop‑Limit
4. TWAP Order (Advanced)
bash
Copy
Edit
# Buy 0.04 BTC in 4 slices every 3 s
python src/main.py twap BTCUSDT BUY 0.04 4 3
All commands print a confirmation and append a JSON record to bot.log.

📝 Logging Example
json
Copy
Edit
{
  "order_id": "2e9b7ac1-b456-45e7-9c5d-7f5a2956c84f",
  "timestamp": 1720991234567,
  "symbol": "BTCUSDT",
  "side": "BUY",
  "type": "MARKET",
  "quantity": 0.01,
  "status": "FILLED",
  "price": "MARKET"
}
🔄 Going Live with Binance Testnet
Register on https://testnet.binancefuture.com and create API keys

pip install python-binance

Add .env:

ini
Copy
Edit
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
BASE_URL=https://testnet.binancefuture.com
Replace mock order dictionaries in market_orders.py / limit_orders.py with:

python
Copy
Edit
order = client.futures_create_order(...)
Everything else (CLI, logs, validation) stays the same—100 % reproducible.

📚 Resources
Official Binance Futures API – https://binance-docs.github.io/apidocs/futures/en/

Optional Historical BTCUSDT Data – Google Drive CSV (back‑testing)

Optional Fear & Greed Index CSV – Google Drive dataset (sentiment filter)

🧭 Future Enhancements
Real API integration (swap mock functions)

Grid or Stop‑Limit strategy in /src/advanced/

Streamlit or Flask dashboard for live monitoring

Use Fear & Greed Index to throttle TWAP buys/sells

Back‑test against historical CSV