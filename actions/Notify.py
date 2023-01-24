from utils.Schedules import scheduleManager
from utils.Messages import sendMarkdownMsg
from utils.Formats import formatNotify, formatSuppressKeyboard
from utils.Alarmjobs import alarmJobManager, AlarmJobManager


async def do(context):
    uuid = context.job.data['uuid']
    idx = context.job.data['idx']
    schedule = scheduleManager.readSchedule(uuid)
    item = schedule["details"][idx]
    for subscriber in schedule["subscribers"]:
        await sendMarkdownMsg(context, subscriber, formatNotify(item), reply_markup=formatSuppressKeyboard(AlarmJobManager.calcAlarmID(uuid, idx, subscriber)))
        alarmJobManager.startAlarm(uuid, idx, subscriber)
