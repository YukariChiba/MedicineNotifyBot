from telegram.ext import CommandHandler
from utils.Schedules import scheduleManager
from utils.Messages import replyMarkdownMsg
from utils.Formats import formatSchedule
from utils.Checker import uuidChecker

enabled = True


def load():
    logger.info('Info command loaded.')


async def help(update, context):
    await replyMarkdownMsg(update, context, '*通过 UUID 查看某个订阅的内容。*\n使用方法：`/info {uuid}`\.')


async def info(update, context):
    if len(context.args) != 1:
        await help(update, context)
        return

    if not uuidChecker(context.args[0]):
        await replyMarkdownMsg(update, context, '错误：`不是合法的 UUID`')
        return  

    uid = update.message.from_user.id

    schedule = scheduleManager.readSchedule(context.args[0])

    if not schedule:
        await replyMarkdownMsg(update, context, '错误：`没有找到该计划`')
        return

    await replyMarkdownMsg(update, context, formatSchedule(schedule))

handlers = [CommandHandler('info', info)]
