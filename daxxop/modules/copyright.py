from pyrogram import Client, filters
from daxxop import daxxop as app
from pyrogram.types import Message

# -----------------------------------------------------

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    if edited_message.from_user.is_admin:
        return
    await edited_message.delete()

@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 

# -----------------------------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ.\n\n ᴀʙ @iam_daxx ʙʜᴀɪ ᴋᴇ ᴅᴍ ᴍᴇ ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊ ᴅᴇ 🍌🍌🍌."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

