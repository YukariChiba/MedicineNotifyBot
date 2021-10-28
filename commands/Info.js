import LocalSchedules from "../utils/LocalSchedules.js";
import { composeSchedulesInfo } from "../utils/Messages.js";

function InfoSchedule(ctx) {
  var msg = ctx.message;
  if (msg.chat.type !== "private") {
    return;
  }
  if (msg.from.is_bot) {
    return;
  }
  const args = msg.text.split(" ");
  if (args.length != 2) {
    ctx.reply("*通过 UUID 查看某个订阅的内容。*\n使用方法：`/info {UUID}`\\.", {
      parse_mode: "MarkdownV2",
    });
    return;
  }
  if (!uuidChecker(args[1])) {
    ctx.reply("Invalid arguments!");
    return;
  }
  if (!LocalSchedules.checkSchedule(args[1])) {
    ctx.reply("Schedule not found!");
    return;
  }
  let schedule = LocalSchedules.getSchedule(args[1]);

  ctx.reply(composeSchedulesInfo(schedule), {
    parse_mode: "MarkdownV2",
  });
}

function uuidChecker(uuid) {
  const regexExp =
    /^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$/gi;
  return regexExp.test(uuid);
}

export default [
  {
    cmd: "info",
    cb: InfoSchedule,
  },
];
