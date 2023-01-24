from telegram.ext import CommandHandler
from utils.Schedules import scheduleManager
from utils.Messages import replyMarkdownMsg

enabled = True


def load():
    logger.info('List command loaded.')


async def help(update, context):
    await replyMarkdownMsg(update, context, '*查看您的订阅列表。*\n使用方法：`/list`.')


async def listfunc(update, context):
    if (len(context.args) != 0):
        await help(update, context)
        return

    uid = update.message.from_user.id

    schedulers = scheduleManager.searchScheduleByUser(uid)

    if not len(schedulers):
        await replyMarkdownMsg(update, context, '错误：`您没有订阅任何计划`')
        return

    await replyMarkdownMsg(update, context, f'您订阅了{len(schedulers)}个提醒：\n' + '\n'.join([f'\- {idx} \[{i[1]["title"]}\]\n`{i[0]}`' for idx, i in enumerate(schedulers)]))

handlers = [CommandHandler('list', listfunc)]
