import dotenv from "dotenv";

import scheduler from "./utils/Scheduler.js"

dotenv.config();

import { Telegraf } from "telegraf";

import commands from "./commands/index.js";

const bot = new Telegraf(process.env.BOT_TOKEN);

commands.forEach((command) => {
  console.log(`Enabling command [${command.cmd}]...`)
  bot.command(command.cmd, command.cb);
});

scheduler.initSchedules(bot)

console.log("Bot is running!")
bot.launch();
process.once("SIGINT", () => bot.stop("SIGINT"));
process.once("SIGTERM", () => bot.stop("SIGTERM"));
