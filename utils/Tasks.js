import LocalSchedules from "./LocalSchedules.js";
import { sendNotification } from "./Messages.js";

function notifyTask(bot, uuid, item) {
  const subscribers = LocalSchedules.getScheduleSubscribers(uuid);
  if (subscribers.length === 0) return;
  subscribers.forEach((subscriber) => {
    sendNotification(subscriber, item, bot);
  });
}

export { notifyTask };
