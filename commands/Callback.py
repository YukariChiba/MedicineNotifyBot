from telegram.ext import CallbackQueryHandler
from utils.Alarmjobs import alarmJobManager
from utils.Messages import sendMarkdownMsg

enabled = True


def load():
    logger.info('Callback command loaded.')


async def suppress(update, context):
    query = update.callback_query
    await query.answer()
    alarmJobManager.stopAlarm(query.data.replace('suppress ', ''))
    await sendMarkdownMsg(context, update.effective_chat.id, '提醒已被标记为完成。')


async def callback(update, context):
    query = update.callback_query
    if query.data.startswith('suppress '):
        await suppress(update, context)
        return

handlers = [CallbackQueryHandler(callback)]
