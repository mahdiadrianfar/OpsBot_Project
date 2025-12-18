import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, SESSION_NAME

PROXY = {
    "scheme": "http",
    "hostname": "127.0.0.1",  # ✅ فقط این
    "port": 12334
}

async def main():
    print("🚀 Starting Telegram client with Windows proxy...")

    app = Client(
        SESSION_NAME,
        api_id=API_ID,
        api_hash=API_HASH,
        proxy=PROXY
    )

    await app.start()
    print("✅ Client started")

    await app.send_message("@mahdiadrianfar", "himan")
    print("✅ Test message sent")

    await asyncio.sleep(2)
    await app.stop()
    print("🛑 Client stopped")


if __name__ == "__main__":
    asyncio.run(main())
