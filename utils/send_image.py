from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from crud.src_bd import SrcDatabase


async def send_img(message: Message, images: list):
    media_builder = MediaGroupBuilder()
    media_group = list()
    for image in images:
        src = SrcDatabase().create_src(image)
        if src:
            media_builder.add_photo(src.file_id)
        else:
            photo = FSInputFile(image)
            media_builder.add_photo(photo)
    media_group = media_builder.build()
    sent_messages = await message.answer_media_group(media=media_group)
    for i, sent_message in enumerate(sent_messages):
        file_id = sent_message.photo[-1].file_id
        original_image = images[i]
        SrcDatabase().update_src(original_image, file_id)
