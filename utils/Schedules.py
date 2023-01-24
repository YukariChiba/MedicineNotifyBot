import json
from uuid import uuid4
import os
import logging


class ScheduleManager:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('ScheduleManager initialized.')
        self.schedules = ScheduleManager.fsReadSchedules()

    def readSchedules(self):
        return self.schedules

    def readSchedule(self, uuid):
        return self.schedules[uuid]

    def createSchedule(self, schedule):
        uuid = ScheduleManager.fsCreateSchedule(schedule)
        self.schedules[uuid] = schedule
        return uuid

    def searchScheduleByUser(self, uid):
        return list(filter(lambda schedule: uid in schedule[1]['subscribers'], self.schedules.items()))

    def checkScheduleByUUID(self, uuid):
        if uuid in self.schedules.keys():
            return True
        else:
            return False

    def addScheduleSubscriber(self, uuid, uid):
        if not uid in self.schedules[uuid]['subscribers']:
            self.schedules[uuid]['subscribers'].append(uid)
            ScheduleManager.fsSaveSchedule(uuid, self.schedules[uuid])

    def delScheduleSubscriber(self, uuid, uid):
        if uid in self.schedules[uuid]['subscribers']:
            self.schedules[uuid]['subscribers'].remove(uid)
            ScheduleManager.fsSaveSchedule(uuid, self.schedules[uuid])

    def fsReadSchedules():
        schedules = {}
        for f in os.listdir('schedules/'):
            if f.endswith('.json'):
                schedules[f.replace('.json', '')] = json.load(
                    open('schedules/' + f))
        return schedules

    def fsReadSchedule(uuid):
        return json.load(open(f'schedules/{uuid}.json'))

    def fsSaveSchedule(uuid, schedule):
        with open(f'schedules/{uuid}.json', 'w') as f:
            json.dump(schedule, f, ensure_ascii=False)

    def fsCreateSchedule(schedule):
        uuid = uuid4()
        with open(f'schedules/{uuid}.json', 'w') as f:
            json.dump(schedule, f, ensure_ascii=False)
        return uuid


scheduleManager = ScheduleManager()
