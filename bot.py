from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- CONFIGURATION (Yahan apni details daalo) ---
API_ID = 21705136  # my.telegram.org se milega
API_HASH = "78730e89d196e160b0f1992018c6cb19" # my.telegram.org se milega
BOT_TOKEN = "8094733589:AAEsY2GFBeNkkwR3Yv9WAADHcvRaq7KgpJw" # BotFather se milega

app = Client("my_test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- EFFECT IDS ---
# Ye IDs Telegram ke server par fixed hoti hain
EFFECTS = {
    "fire": 5104841245755180586,
    "heart": 5159385139981059251,
    "thumbs_up": 5107584321108051014,
    "party": 5046509860389126442
}

@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Ye wo formatting hai jo tumne pehle puchi thi (Blue Quote Line)
    text_message = (
        "> **❝ TESTING BOT MODE ❞**\n"
        "> **◉ SELECT AN EFFECT BELOW**\n"
        "> **◉ CLICK BUTTON TO TEST** 🔥"
    )

    # Buttons banaye hain taaki click karke test kar sako
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔥 Fire Effect", callback_data="fire"),
            InlineKeyboardButton("❤️ Heart Effect", callback_data="heart")
        ],
        [
            InlineKeyboardButton("👍 Thumbs Up", callback_data="thumbs_up"),
            InlineKeyboardButton("🎉 Party", callback_data="party")
        ]
    ])

    await message.reply_text(
        text=text_message,
        reply_markup=buttons
    )

# Button click karne par ye chalega
@app.on_callback_query()
async def handle_callbacks(client, callback_query):
    effect_name = callback_query.data
    
    if effect_name in EFFECTS:
        effect_id = EFFECTS[effect_name]
        
        # Ye hai wo MAIN magic line jisse animation aati hai
        await client.send_message(
            chat_id=callback_query.message.chat.id,
            text=f"Ye raha tumhara **{effect_name.upper()}** effect! ✨",
            message_effect_id=effect_id  # <-- Yahan ID lagti hai
        )
        
        await callback_query.answer("Effect Sent! Check chat.")
    else:
        await callback_query.answer("Unknown effect")

print("Bot start ho gaya hai bhai! Telegram par /start bhejo.")
app.run()
