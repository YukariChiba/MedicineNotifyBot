import LocalSchedules from "../utils/LocalSchedules.js";
import { composeSchedulesListInfo } from "../utils/Messages.js";

function ListSchedules(ctx) {
  var msg = ctx.message;
  if (msg.chat.type !== "private") {
    return;
  }
  if (msg.from.is_bot) {
    return;
  }
  const args = msg.text.split(" ");
  if (args.length != 1) {
    ctx.reply("*查看您的订阅列表。*\n使用方法：`/list`\\.", {
      parse_mode: "MarkdownV2",
    });
    return;
  }
  let schedules = LocalSchedules.getUIDSchedules(msg.from.id);

  ctx.reply(composeSchedulesListInfo(schedules), {
    parse_mode: "MarkdownV2",
  });
}

export default [
  {
    cmd: "list",
    cb: ListSchedules,
  },
];
