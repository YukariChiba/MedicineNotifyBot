import fs from "fs";
import path from "path";
import { v4 as uuidv4 } from "uuid";

function checkSchedule(uuid) {
  const path = `./schedules/${uuid}.json`;
  try {
    if (fs.existsSync(path)) {
      return true;
    }
  } catch (err) {
    return false;
  }
}

function getUIDSchedules(uid) {
  let scheduleList = getSchedules();
  let subscribedScheduleList = scheduleList.filter((ss) =>
    ss.subscribers.includes(uid)
  );
  return subscribedScheduleList;
}

function getSchedules() {
  var scheduleList = [];
  const jsonsInDir = fs
    .readdirSync("./schedules")
    .filter((file) => path.extname(file) === ".json");
  jsonsInDir.forEach((file) => {
    const fileData = fs.readFileSync(path.join("./schedules", file));
    const json = JSON.parse(fileData.toString());
    json.uuid = file.split(".")[0];
    scheduleList.push(json);
  });
  return scheduleList;
}

function getScheduleSubscribers(uuid) {
  const schedule = getSchedule(uuid);
  return schedule.subscribers;
}

function addScheduleSubscriber(uuid, uid) {
  const schedule = getSchedule(uuid);
  schedule.subscribers.push(uid);
  saveSchedule(schedule, uuid);
  return schedule.title;
}

function delScheduleSubscriber(uuid, uid) {
  const schedule = getSchedule(uuid);
  var idx = schedule.subscribers.indexOf(uid);
  if (idx > -1) schedule.subscribers.splice(idx, 1);
  else return null;
  saveSchedule(schedule, uuid);
  return schedule.title;
}

function saveSchedule(schedule, uuid = null) {
  if (!uuid) uuid = uuidv4();
  let data = JSON.stringify(schedule, null, 4);
  fs.writeFileSync(`./schedules/${uuid}.json`, data);
  return uuid;
}

function getSchedule(uuid) {
  const fileData = fs.readFileSync(path.join(`./schedules/${uuid}.json`));
  return JSON.parse(fileData.toString());
}

export default {
  checkSchedule,
  getSchedules,
  getSchedule,
  getScheduleSubscribers,
  addScheduleSubscriber,
  delScheduleSubscriber,
  getUIDSchedules,
};
