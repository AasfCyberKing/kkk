import os 
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
import tgcrypto
import io
from thumbnail import hb.jpg

from pyrogram.types import Message
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup)
HB = Client(
    "MSG_DELETING Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """**
HI {}, 
I AM A SIMPLE 
TEXT TO FILE BOT 
JUST SENT YOUR CODE OR TEXT MESSAGE 
THEN I WILL CONVERT IT INTO FILE

MADE BY @TELSABOTS**"""

HELP_TEXT = """**
SENT ANY TEXT MESSAGE.......

THEN REPLY WITH ANY /COMMAND

eg :- /python

PRESS /LIST COMMAND TO KNOW ABOUT
CUREENTLY SUPPORTED EXTENSIONS

MADE BY @TELSABOTS**
"""

ABOUT_TEXT = """
 🤖<b>BOT :MEDIA INFO 🤖</b>

📢<b>CHANNEL :</b>@TELSA BOTS

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

"""

list_text = """**Language ➲ Language COMMAND
PYTHON➲  /python
 JAVA ➲  /java
HTML ➲ /html
CSS ➲ /css
PHP ➲ /php
SASS ➲ /sass
PERL ➲ /perl
SHELL ➲ /shell
MATLAB ➲ /matlab
KIVY ➲ /kivy
KOTLIN ➲ /kotlin
JAVA SCRIPT ➲  /js
SQL ➲  /sql
SWIFT ➲  /swift
SAS ➲ /sas
XML ➲ /xml
RUBY ➲ /ruby
GO ➲ /go
RUST ➲ /rust
YAML ➲ /yaml
DOCKER FILE ➲ /docker
C PROGRAMMING ➲ /C
MARK DOWN ➲ /markdown **"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict'),
        InlineKeyboardButton('⭐️VOTE⭐️', url='https://t.me/BotsArchive/2431')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

list_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()


result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

result_text = """**JOIN @TELSABOTS"""

@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
@HB.on_message(filters.command(["list"]))
async def about_message(bot, update):
    text = list_text
    reply_markup = list_buttons
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
@HB.on_inline_query()
async def answer(client, inline_query):
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="MOVIES CHANNEL",
                input_message_content=InputTextMessageContent(
                    "**NEW MOVIES CHANNEL**"
                ),
                
                description="OUR CHANNEL TO DOWNLOAD NEW MOVIES",
                thumb_url="https://telegra.ph/file/e8a39b06fabbfac6bce8f.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "📢CHANNEL📢",
                            url="https://t.me/+UZzc1ZqHvYXaLeNf"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="GROUP",
                input_message_content=InputTextMessageContent(
                    "**<i>MOVIE REQUESTING GROUP</i>**"
                ),
                
                description="A GROUP TO REQUEST ALL MOVIES ",
                thumb_url="https://telegra.ph/file/e8a39b06fabbfac6bce8f.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "GROUP",
                            url="https://t.me/+UZzc1ZqHvYXaLeNf"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
    )
import asyncio
thumbnail="hb.jpg"

wait="WAIT FOR 10 SECOND"
@HB.on_message(filters.text & filters.command(["docker"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "DOCKER.dockerfile"
    await client.send_document(msg.chat.id, file_obj, thumbs=thumbnail, reply_markup=reply_markup, caption=result_text)
    await asynico.sleep(60)
    await client.reply_text(msg.chat.id, text=wait,reply_markup=reply_markup)

@HB.on_message(filters.text & filters.command(["php"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "site.php"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
    await asynico.sleep(60)
    await client.reply_text(msg.chat.id, text=wait,reply_markup=reply_markup)
    
@HB.on_message(filters.text & filters.command(["plain"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "msg.txt"
    await client.send_document(msg.chat.id, file_obj, thumb=thumbnail, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["YAML"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "HB.yml"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["swift"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "HB.swift"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["python"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "main.py"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["sql"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "MY.sql"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["C"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "main.c"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)


@HB.on_message(filters.text & filters.command(["ruby"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "RUBY.rb"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["markdown"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "README.md"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
    
@HB.on_message(filters.text & filters.command(["html"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "index.html"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["java"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "app.java"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["js"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "script.js"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["css"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "style.css"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["sass"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "STYLE.scss"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["perl"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "file.perl"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
@HB.on_message(filters.text & filters.command(["xml"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "PROJECT.py"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
    
@HB.on_message(filters.text & filters.command(["sas"]))
async def echo_document(client: Client, msg: Message):
    reply_markup =result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "SAS .sas"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
    
@HB.on_message(filters.text & filters.command(["shell"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "SHELL.cgi"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["matlab"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "MATLAB.matlab"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["kotlin"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "KOTLIN.kt"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["kivy"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "thelab.kv"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)
                            
@HB.on_message(filters.text & filters.command(["go"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "FILE.go"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["rust"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "RUST.rust"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.text & filters.command(["php"]))
async def echo_document(client: Client, msg: Message):
    reply_markup = result_buttons
    reply_markup = result_buttons
    file_obj = io.BytesIO(bytes(msg.reply_to_message.text, "utf-8"))
    file_obj.name = "site.php"
    await client.send_document(msg.chat.id, file_obj, reply_markup=reply_markup, caption=result_text)

@HB.on_message(filters.private & filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "**...**"
    )
    await status_message.edit(
        "**PLZ WAIT...**"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>❇️FIRST NAME:</b> {from_user.first_name}\n\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>✳️LAST NAME✳:</b> {last_name}\n\n"
    message_out_str += f"<b> 🆔ID :</b> <code>{from_user.id}</code>\n\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str += f"<b>🗃DC :</b> <code>{dc_id}</code>\n\n"
    message_out_str += f"<b>🈯️USER NAME:</b> @{username}\n\n"
    message_out_str += f"<b>🔗USER LINK:</b> <a href='tg://user?id={from_user.id}'><b>LINK </b></a>\n\n"
    if message.chat.type in (("supergroup", "channel")):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🧑‍💻DEV🧑‍💻', url="https://t.me/alluaddict"),
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close_data')
            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode="html",
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode="html",
            disable_notification=True
        )
    await status_message.delete()
    
print("HB")

HB.run()
