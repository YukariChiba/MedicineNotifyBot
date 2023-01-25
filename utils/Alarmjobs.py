from utils.Schedules import scheduleManager
import logging


class AlarmJobManager:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('AlarmJobManager initialized.')
        self.jobs = {}
        self.counter = {}
        self._job_queue = None

    def init(self, queue):
        self._job_queue = queue

    def calcAlarmID(uuid, idx, uid):
        return f'{str(uuid)}.{str(idx)}.{str(uid)}'

    def stopAlarm(self, alarm_id):
        if alarm_id in self.jobs:
            self.jobs[alarm_id].schedule_removal()
            self.jobs.pop(alarm_id, None)
            self.counter[alarm_id] = -1

    def startAlarm(self, uuid, idx, uid):
        import actions.Alarm
        alarm_id = AlarmJobManager.calcAlarmID(uuid, idx, uid)
        if alarm_id in self.jobs.keys():
            return
        self.counter[alarm_id] = 2
        self.jobs[alarm_id] = self._job_queue.run_custom(
            actions.Alarm.do,
            data={
                "uuid": uuid,
                "idx": idx,
                "uid": uid
            },
            job_kwargs={
                'trigger': 'cron',
                'minute': '*/3',
            },
        )


alarmJobManager = AlarmJobManager()
