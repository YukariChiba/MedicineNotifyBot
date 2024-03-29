import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Defaults
from dotenv import load_dotenv
import commands
import pytz
import os
from utils.Cronjobs import jobManager
from utils.Alarmjobs import alarmJobManager

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':

    import logging.config
    # logging.config.fileConfig('logging.conf')

    defaults = Defaults(tzinfo=pytz.timezone(
        os.getenv("TZ", "Asia/Hong_Kong")))

    if not os.getenv("BOTTOKEN"):
        logging.error("Bot token not defined!")
        exit(1)

    application = ApplicationBuilder().token(
        os.getenv("BOTTOKEN")).defaults(defaults).build()

    for command in commands.__all__:
        if command.enabled:
            command.load()
            for handler in command.handlers:
                application.add_handler(handler)

    jobManager.init(application.job_queue)
    alarmJobManager.init(application.job_queue)

    application.run_polling()
