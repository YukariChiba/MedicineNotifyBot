from telegram.ext import CommandHandler

enabled = True


def load():
    logger.info('Start command loaded.')


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

handlers = [CommandHandler('start', start)]
