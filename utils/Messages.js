import fs from "fs";
import path from "path";

function readTemplate(filename) {
  return fs.readFileSync(path.resolve(`templates/${filename}.md`), "utf8");
}

function composeSchedulesInfo(item) {
  let send_msg = readTemplate("info/header");
  send_msg = send_msg
    .replace("{title}", item.title)
    .replace("{subscribers}", item.subscribers.length);
  item.details.forEach((schedule, idx) => {
    send_msg =
      send_msg +
      readTemplate("info/interval")
        .replace("{interval}", schedule.interval)
        .replace("{index}", idx + 1);
    send_msg = send_msg + composeScheduleInfo(schedule.contents);
  });
  return send_msg;
}

function composeSchedulesListInfo(schedulesList) {
  let send_msg = readTemplate("list/header").replace(
    "{count}",
    schedulesList.length
  );
  schedulesList.forEach((schedules, index) => {
    send_msg =
      send_msg +
      readTemplate("list/item")
        .replace("{index}", index + 1)
        .replace("{title}", schedules.title)
        .replace("{uuid}", schedules.uuid);
  });
  return send_msg;
}

function composeScheduleInfo(items) {
  let send_msg = "";
  items.forEach((content) => {
    let content_msg = readTemplate("notify/part");
    if (content.desc) content_msg = content_msg + readTemplate("notify/desc");
    content_msg = content_msg
      .replace("{name}", content.name)
      .replace("{amount}", content.amount)
      .replace("{desc}", content.desc);
    send_msg = send_msg + content_msg;
  });
  return send_msg;
}

function sendNotification(to, item, bot) {
  let send_msg = readTemplate("notify/header");
  send_msg = send_msg + composeScheduleInfo(item.contents);
  bot.telegram.sendMessage(to, send_msg, {
    parse_mode: "MarkdownV2",
  });
}

export {
  readTemplate,
  sendNotification,
  composeSchedulesInfo,
  composeSchedulesListInfo,
};
