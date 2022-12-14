from __future__ import unicode_literals

import os
import requests
import aiohttp
import asyncio
import math
import time

import wget
import aiofiles

from pyrogram import filters, Client, enums
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import youtube_dl
import requests




@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = gettext(message)

    pablo = await client.send_message(
        message.chat.id, f"**π΅πΈπ½π³πΈπ½πΆ ππΎππ ππΈπ³π΄πΎ** `{urlissed}`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax Please Check help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(event, f"**π³ππ πππππ π΅πππππ πΏπππππ πππ’ π°ππππ..β₯οΈ** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""
**ππΈππ»π΄ :** [{thum}]({mo})
**ππ΄πππ΄πππ΄π³ π±π :** {message.from_user.mention}
**@α΄α΄α΄α΄_α΄α΄α΄α΄**
"""
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
