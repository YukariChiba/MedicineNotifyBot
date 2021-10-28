import dotenv from "dotenv";

import scheduler from "./utils/Scheduler.js"

dotenv.config();

import { Telegraf } from "telegraf";

import commands from "./commands/index.js";

const bot = new Telegraf(process.env.BOT_TOKEN);

commands.forEach((command) => {
  bot.command(command.cmd, command.cb);
});

scheduler.initSchedules(bot)

bot.launch();
process.once("SIGINT", () => bot.stop("SIGINT"));
process.once("SIGTERM", () => bot.stop("SIGTERM"));
