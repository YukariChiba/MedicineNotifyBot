function Placeholder(ctx) {
  var msg = ctx.message;
  if (msg.chat.type !== "private") {
    return;
  }
  if (msg.from.is_bot) {
    return;
  }
  ctx.reply("_该功能尚未可用。_", {
    parse_mode: "MarkdownV2",
  });
}

export default [
  {
    cmd: "create",
    cb: Placeholder,
  },
];
