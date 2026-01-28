from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- CONFIGURATION ---
API_ID = 21705136 
API_HASH = "78730e89d196e160b0f1992018c6cb19"
BOT_TOKEN = "8094733589:AAEsY2GFBeNkkwR3Yv9WAADHcvRaq7KgpJw"

app = Client("my_test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- EFFECT IDS (Screen par aag/dil udne wala) ---
EFFECTS = {
    "fire": 5104841245755180586,
    "heart": 5159385139981059251,
}

@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Niche dekho text me maine ek emoji ID lagayi hai.
    # Ye ID kisi animated emoji ki hoti hai. 
    # Aapko apni pasand ke animated emoji ki ID nikalni padegi.
    
    # Example Custom Emoji ID: 5465665476971471368 (Ye ek random animated emoji hai)
    
    txt = (
        "> **❝ TESTING BOT MODE ❞**\n"
        "> **◉ CHECK ANIMATION**\n"
        "> **◉ RIGHT SIDE EMOJI ** <emoji id=5465665476971471368>👋</emoji>" 
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Test Fire Effect", callback_data="fire")],
        [InlineKeyboardButton("❤️ Test Heart Effect", callback_data="heart")]
    ])

    await message.reply_text(
        text=txt,
        reply_markup=buttons
    )

@app.on_callback_query()
async def handle_callbacks(client, callback_query):
    effect_name = callback_query.data
    if effect_name in EFFECTS:
        try:
            await client.send_message(
                chat_id=callback_query.message.chat.id,
                text=f"Ye raha effect! ✨",
                message_effect_id=EFFECTS[effect_name] # Ye tabhi chalega jab Pyrofork install hoga
            )
            await callback_query.answer("Sent!")
        except Exception as e:
            await callback_query.answer(f"Error: {e}", show_alert=True)

print("Bot Started... Pyrofork install karna mat bhulna!")
app.run()
