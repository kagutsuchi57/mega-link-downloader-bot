
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<i>Hello there,</i>
    
I am a <b><em>Mega Link Downloader</em></b> bot!
Just enter your mega.nz link and I will return the file/video to you!😇
Press /help for more details!
"""

    DOWNLOAD_START = """<em><b>Downloading File To My DC</b></em>"""
    UPLOAD_START = " ǝlıɟ ɹnoʎ ɓuıpɐoldn ʍoN 📤..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥𝘦𝘥 𝘪𝘯 <b>{}</b> 𝘴𝘦𝘤𝘰𝘯𝘥𝘴.\n𝘜𝘱𝘭𝘰𝘢𝘥𝘦𝘥 𝘪𝘯 <b>{}</b> 𝘴𝘦𝘤𝘰𝘯𝘥𝘴."
    SAVED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗜𝘀 𝗦𝗮𝘃𝗲𝗱. 𝗧𝗵𝗶𝘀 𝗜𝗺𝗮𝗴𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗨𝘀𝗲𝗱 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗡𝗲𝘅𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝘀 📁.\n\n<i>If you want to delete it send\n /deletethumbnail anytime!</i>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗖𝗹𝗲𝗮𝗿𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ❌.\n<i>You will now get an auto generated thumbnail for your video uploads!</i>"

    HELP_USER = f""" 𝐇𝐢 𝐈 𝐚𝐦 𝐚 𝐌𝐞𝐠𝐚 𝐋𝐢𝐧𝐤 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭..
 
𝐇𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞\n\n
𝐉𝐮𝐬𝐭 𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚 𝐦𝐞𝐠𝐚.𝐧𝐳 𝐟𝐢𝐥𝐞 𝐥𝐢𝐧𝐤! 
- 𝐅𝐨𝐥𝐝𝐞𝐫 𝐥𝐢𝐧𝐤𝐬 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝.
- 𝐘𝐨𝐮𝐫 𝐥𝐢𝐧𝐤 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐯𝐚𝐥𝐢𝐝(𝐧𝐨𝐭 𝐞𝐱𝐩𝐢𝐫𝐞𝐝 𝐨𝐫 𝐛𝐞𝐞𝐧 𝐫𝐞𝐦𝐨𝐯𝐞𝐝) 𝐚𝐧𝐝 𝐬𝐡𝐨𝐮𝐥𝐝 𝐧𝐨𝐭 𝐛𝐞 𝐩𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐩𝐫𝐨𝐭𝐞𝐜𝐭𝐞𝐝 𝐨𝐫 𝐞𝐧𝐜𝐫𝐲𝐩𝐭𝐞𝐝 𝐨𝐫 𝐩𝐫𝐢𝐯𝐚𝐭𝐞!\n
-<𝐛>𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐚 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐮𝐩𝐥𝐨𝐚𝐝𝐬 𝐬𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨.
𝐈𝐟 𝐲𝐨𝐮 𝐝𝐨𝐧'𝐭 𝐬𝐞𝐧𝐝 𝐚 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨/𝐟𝐢𝐥𝐞 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐰𝐢𝐭𝐡 𝐚𝐧 𝐚𝐮𝐭𝐨 𝐠𝐞𝐧𝐚𝐫𝐚𝐭𝐞𝐝 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨.\n
𝐩𝐫𝐞𝐬𝐬 /deletethumbnail 𝐢𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐝𝐞𝐥𝐞𝐭𝐞 𝐭𝐡𝐞 𝐩𝐫𝐞𝐯𝐢𝐨𝐮𝐬𝐥𝐲 𝐬𝐚𝐯𝐞𝐝 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥.
(𝐓𝐡𝐞𝐧 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐰𝐢𝐭𝐡 𝐚𝐧 𝐚𝐮𝐭𝐨-𝐠𝐞𝐧𝐚𝐫𝐚𝐭𝐞𝐝 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥!)\n\n
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐥𝐢𝐧𝐤𝐬 𝐰𝐡𝐢𝐜𝐡 𝐚𝐫𝐞 𝐛𝐢𝐠𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 𝟐𝐆𝐁 𝐟𝐫𝐨𝐦 𝐦𝐞 𝐭𝐨𝐨! 𝐃𝐮𝐞 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐏𝐈 𝐥𝐢𝐦𝐢𝐭𝐬 𝐈 𝐜𝐚𝐧'𝐭 𝐮𝐩𝐥𝐨𝐚𝐝 𝐟𝐢𝐥𝐞𝐬 𝐰𝐡𝐢𝐜𝐡 𝐚𝐫𝐞 𝐛𝐢𝐠𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 𝟐𝐆𝐁 𝐬𝐨 𝐈 𝐰𝐢𝐥𝐥 𝐬𝐩𝐥𝐢𝐭 𝐬𝐮𝐜𝐡 𝐟𝐢𝐥𝐞𝐬 𝐚𝐧𝐝 𝐮𝐩𝐥𝐨𝐚𝐝 𝐭𝐡𝐞𝐦 𝐭𝐨 𝐲𝐨𝐮!"""
