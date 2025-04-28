from pyrogram import Client, filters

@Client.on_message(filters.private & filters.text & ~filters.command(["start", "help"]))
async def block_pm_text(client, message):
    await message.reply_text(
        "❌ Searching in private chat is not allowed.\n\n"
        "Please search in our group: @moviesandseries36",
        quote=True
    )
