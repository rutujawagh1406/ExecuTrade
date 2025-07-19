# ExecuTrade 🪙📈
A CLI-based Binance USDT-M Futures trading bot built with Python and Flask, capable of executing Market and Limit orders using Binance's REST API. Designed for both real and mock environments with modular logic, logging, and robust configuration handling.

## 🚀 Features
- ✅ Market and Limit Order execution
- ⏳ Support for mock trading (no real money involved)
- 📡 Flask-based backend for webhook/API integration
- 📘 Detailed logging (`bot.log`) for trade tracking
- 🔐 Secure API key management via `.env`

## ⚙️ Tech Stack
- **Language**: Python
- **Frameworks**: Flask
- **Tools**: Binance API, dotenv, ngrok (for testing)

## 📁 Project Structure
ExecuTrade/
│
├── src/ # Bot logic and utils
├── .env # Secure API keys
├── bot.log # Logs of all activity
├── README.md
└── ExecuTrade.pdf # Project documentation/report

bash
Copy
Edit

## 📸 Screenshots
(Add screenshots of CLI & Flask UI or ngrok link here)

## 🛠️ Setup
```bash
git clone https://github.com/rutujawagh1406/ExecuTrade.git
cd ExecuTrade
pip install -r requirements.txt
Update .env with your Binance API keys and run:

bash
Copy
Edit
python src/main.py
📬 Contact
For feedback or questions, reach me at waghrutujamanish@gmail.com
