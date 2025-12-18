# main.py
# ===============================
# Main entry for Telegram API 8
# ===============================

import asyncio
from telethon import TelegramClient

from config import API_ID, API_HASH, SESSION_NAME

# 🔹 ایمپورت ربات‌ها
from bots import bot_1
from bots import bot_2
from bots import bot_3


async def main():
    #  ساخت کلاینت تلگرام
    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH
    )

    #  استارت کلاینت (اولین بار کد می‌خواد)
    await client.start()
    print("✅ Telegram client started successfully")

    #  ثبت هندلرهای هر ربات
    await bot_1.register(client)
    await bot_2.register(client)
    await bot_3.register(client)

    print("🤖 All bots registered and running...")

    #  اجرای دائم
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
