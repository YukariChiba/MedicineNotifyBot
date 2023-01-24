from telegram.ext import CommandHandler
from utils.Schedules import scheduleManager
from utils.Messages import replyMarkdownMsg
from utils.Formats import formatSchedule

enabled = True


def load():
    logger.info('Debug command loaded.')


async def help(update, context):
    await replyMarkdownMsg(update, context, '*调试选项。*\n使用方法：`/debug {subcommand}`.')


async def debug(update, context):
    if (len(context.args) != 1):
        await help(update, context)
        return

handlers = [CommandHandler('debug', debug)]
