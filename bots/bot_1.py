# bots/bot_1.py

from pyrogram import Client



TARGET_CHAT_ID = "@mahdiadrianfar"
# TARGET_CHAT_ID = 123456789


async def register(app: Client):
    await app.send_message(
        chat_id=TARGET_CHAT_ID,
        text="himan"
    )
    print(f"✅ Test message sent to {TARGET_CHAT_ID}")
