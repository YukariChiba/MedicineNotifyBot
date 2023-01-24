from utils.Schedules import scheduleManager
import logging


class JobManager:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('JobManager initialized.')
        self.jobs = {}
        self._job_queue = None

    def stopSchedule(self, uuid):
        for job in self.jobs[uuid]:
            job.schedule_removal()
        self.jobs[uuid].clear()

    def checkSchedule(self, uuid):
        schedule = scheduleManager.readSchedule(uuid)
        if len(schedule["subscribers"]) == 0:
            self.stopSchedule(uuid)
        elif len(self.jobs[uuid]) == 0:
            self.startSchedule(schedule, uuid)

    def startSchedule(self, schedule, uuid):
        import actions.Notify
        for idx, it in enumerate(schedule["details"]):
            cronkey = it["interval"].split(' ')
            if len(cronkey) != 5:
                self.logger.warning(
                    f'{it["interval"]} is not a valid crontab string!')
                continue
            cron_minute = cronkey[0]
            cron_hour = cronkey[1]
            cron_dayofmonth = cronkey[2]
            cron_month = cronkey[3]
            cron_dayofweek = cronkey[4]
            self.jobs[uuid].append(
                self._job_queue.run_custom(
                    actions.Notify.do,
                    data={
                        "uuid": uuid,
                        "idx": idx
                    },
                    job_kwargs={
                        'trigger': 'cron',
                        'day': cron_dayofmonth,
                        'day_of_week': cron_dayofweek,
                        'hour': cron_hour,
                        'month': cron_month,
                        'minute': cron_minute,
                    },
                )
            )

    def init(self, queue):
        self._job_queue = queue
        schedules = scheduleManager.readSchedules()
        for schedule_pair in schedules.items():
            schedule_uuid = schedule_pair[0]
            schedule = schedule_pair[1]
            self.jobs[schedule_uuid] = []
            if len(schedule["subscribers"]) == 0:
                continue
            self.startSchedule(schedule, schedule_uuid)


jobManager = JobManager()
