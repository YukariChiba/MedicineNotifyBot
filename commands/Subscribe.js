import LocalSchedules from "../utils/LocalSchedules.js";

function SubscribeSchedule(ctx) {
  var msg = ctx.message;
  if (msg.chat.type !== "private") {
    return;
  }
  if (msg.from.is_bot) {
    return;
  }
  const args = msg.text.split(" ");
  if (args.length != 2) {
    ctx.reply("*通过 UUID 订阅一个通知。*\n使用方法：`/subscribe {UUID}`\\.", {
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
  let scheduleTitle = LocalSchedules.addScheduleSubscriber(
    args[1],
    msg.from.id
  );
  ctx.reply(`成功订阅 [${scheduleTitle}]!`);
}

function uuidChecker(uuid) {
  const regexExp =
    /^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$/gi;
  return regexExp.test(uuid);
}

export default [
  {
    cmd: "subscribe",
    cb: SubscribeSchedule,
  },
];
