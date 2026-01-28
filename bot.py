from pyrogram import Client, filters
from pyrogram.enums import ParseMode

# --- CONFIG ---
API_ID = 21705136 
API_HASH = "78730e89d196e160b0f1992018c6cb19"
BOT_TOKEN = "8094733589:AAEsY2GFBeNkkwR3Yv9WAADHcvRaq7KgpJw"

app = Client("my_test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("test"))
async def test_animation(client, message):
    # Text ke right side me animation ke liye 'emoji id' lagani padti hai
    # Niche dekho 'id=543...'. Ye ek animated star emoji hai.
    text = (
        "> **TESTING ANIMATION**\n"
        "> **Ye raha right corner animation** <emoji id=5431443013404434241>✨</emoji>"
    )
    
    await message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN
    )

print("Bot is running...")
app.run()
