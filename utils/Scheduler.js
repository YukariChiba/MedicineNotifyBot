import cron from "node-cron";
import LocalSchedules from "../utils/LocalSchedules.js";
import { notifyTask } from "./Tasks.js";

if (!global.scheduleList) {
  global.scheduleList = [];
}

if (!global.schedulerList) {
  global.schedulerList = {};
}

function initSchedules(bot) {
  global.scheduleList = LocalSchedules.getSchedules();
  global.scheduleList.forEach((schedule) => {
    var schedulerItemList = [];
    schedule.details.forEach((scheduleItem) => {
      schedulerItemList.push(
        cron.schedule(
          scheduleItem.interval,
          () => notifyTask(bot, schedule.uuid, scheduleItem),
          {
            scheduled: true,
            timezone: "Asia/Hong_Kong",
          }
        )
      );
    });
    global.schedulerList[schedule.uuid] = schedulerItemList;
  });
}

export default { initSchedules };
