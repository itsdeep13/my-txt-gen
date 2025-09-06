import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "27473563"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "bc2ea0765ac96bb474891b0243f44390")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8360763217:AAG8EuJ9vdsMB1YTKAgNihOldq3_KjIxBUw")

OWNER_ID = int(os.environ.get("OWNER_ID", "6363345131"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "6363345131").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Deep:<XDeep>@cluster0.c8youpz.mongodb.net/?retryWrites=true&w=majority")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
