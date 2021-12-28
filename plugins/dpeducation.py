import asyncio
from userge import userge, filters, Message

@userge.on_filters(filters.chat(-1001772754530) & filters.incoming &filters.text & filters.regex(pattern=r"(?i).*උසස් පෙළ"), allow_via_bot=False)
async def dpeducational(message: Message):
    await userge.send_message(-1001527521324, f"**{message.text}**", parse_mode="md")

@userge.on_filters(filters.chat(-1001772754530) & filters.incoming &filters.text & filters.regex(pattern=r"(?i).*ශිෂ්‍යත්ව"), allow_via_bot=False)
async def dpeducationscholar(message: Message):
    await userge.send_message(-1001584884507, f"**{message.text}**", parse_mode="md")

@userge.on_filters(filters.chat(-1001772754530) & filters.incoming &filters.text & filters.regex(pattern=r"(?i).*සාමාන්‍ය පෙළ"), allow_via_bot=False)
async def dpeducationol(message: Message):
    await userge.send_message(-1001268474395, f"**{message.text}**", parse_mode="md")
