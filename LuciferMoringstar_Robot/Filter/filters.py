from pyrogram import Client, filters




@Client.on_message(filters.regex("Hi") | filters.regex("hi"))
async def regex(bot, msg):
    await msg.reply_text("soon")
