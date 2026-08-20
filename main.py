import asyncio
import random
from telegram import Bot

TOKEN = "ඔබේ_BOT_TOKEN_එක"
CHAT_ID = "@ඔබේ_CHANNEL_NAME"

bot = Bot(token=TOKEN)

async def send_signals():
    while True:
        mult = round(random.uniform(1.60, 3.80), 2)
        msg = f"🚀 **AVIATOR SIGNAL** 🚀\n\n🎯 Target: **{mult}x**\n💡 Safe: **1.30x**"
        try:
            await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
        except Exception as e:
            print(e)
        await asyncio.sleep(300) # තත්පර 300 (මිනිත්තු 5) සැරයක් යවයි

if __name__ == "__main__":
    asyncio.run(send_signals())
