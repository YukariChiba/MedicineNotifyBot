import { readTemplate } from "../utils/Messages.js";

function Help(ctx) {
  var msg = ctx.message;
  if (msg.chat.type !== "private") {
    return;
  }
  if (msg.from.is_bot) {
    return;
  }
  ctx.reply(readTemplate("help/msg"), {
    parse_mode: "MarkdownV2",
  });
}

export default [
  {
    cmd: "help",
    cb: Help,
  },
];
