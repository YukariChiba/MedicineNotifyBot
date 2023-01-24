from utils.Schedules import scheduleManager
from utils.Messages import sendMarkdownMsg
from utils.Formats import formatAlarm, formatSuppressKeyboard
from utils.Alarmjobs import alarmJobManager, AlarmJobManager


async def do(context):
    uuid = context.job.data['uuid']
    uid = context.job.data['uid']
    idx = context.job.data['idx']
    schedule = scheduleManager.readSchedule(uuid)
    item = schedule["details"][idx]
    alarm_id = AlarmJobManager.calcAlarmID(uuid, idx, uid)
    await sendMarkdownMsg(context, uid, formatAlarm(item, alarmJobManager.counter[alarm_id]), reply_markup=formatSuppressKeyboard(AlarmJobManager.calcAlarmID(uuid, idx, uid)))
    alarmJobManager.counter[alarm_id] = alarmJobManager.counter[alarm_id] + 1
    if alarmJobManager.counter[alarm_id] >= 7:
        alarmJobManager.stopAlarm(uuid, idx, uid)
