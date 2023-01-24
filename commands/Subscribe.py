from telegram.ext import CommandHandler

from utils.Schedules import scheduleManager
from utils.Cronjobs import jobManager
from utils.Messages import replyMarkdownMsg
from utils.Checker import uuidChecker

enabled = True


def load():
    logger.info('Subscibe command loaded.')


async def help(update, context):
    await replyMarkdownMsg(update, context, '**通过 UUID 订阅某个计划。\n使用方法：`/subscribe {UUID}.`')


async def unhelp(update, context):
    await replyMarkdownMsg(update, context, '**通过 UUID 取消订阅某个计划。\n使用方法：`/unsubscribe {UUID}.`')


async def unsubscribe(update, context):
    if (len(context.args) != 1):
        await unhelp(update, context)
        return

    if not uuidChecker(context.args[0]):
        await replyMarkdownMsg(update, context, '错误：`不是合法的 UUID`')
        return

    if not scheduleManager.checkScheduleByUUID(context.args[0]):
        await replyMarkdownMsg(update, context, '错误：`UUID 不存在`')
        return

    scheduleManager.delScheduleSubscriber(
        context.args[0], update.message.from_user.id)
    jobManager.checkSchedule(context.args[0])
    schedule = scheduleManager.readSchedule(context.args[0])
    await replyMarkdownMsg(update, context, f'您已成功取消订阅 **{schedule["title"]}**')


async def subscribe(update, context):
    if (len(context.args) != 1):
        await help(update, context)
        return

    if not uuidChecker(context.args[0]):
        await replyMarkdownMsg(update, context, '错误：`不是合法的 UUID`')
        return

    if not scheduleManager.checkScheduleByUUID(context.args[0]):
        await replyMarkdownMsg(update, context, '错误：`UUID 不存在`')
        return

    uid = update.message.from_user.id

    if len(scheduleManager.searchScheduleByUser(uid)) > 5:
        await replyMarkdownMsg(update, context, '错误：`您最多订阅 5 个计划`')
        return

    scheduleManager.addScheduleSubscriber(
        context.args[0], uid)
    jobManager.checkSchedule(context.args[0])
    schedule = scheduleManager.readSchedule(context.args[0])
    await replyMarkdownMsg(update, context, f'您已成功订阅 **{schedule["title"]}**')

handlers = [CommandHandler('subscribe', subscribe),
            CommandHandler('unsubscribe', unsubscribe)]
