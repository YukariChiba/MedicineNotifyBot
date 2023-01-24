import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv
import commands
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

    application = ApplicationBuilder().token(os.getenv("BOTTOKEN")).build()

    for command in commands.__all__:
        if command.enabled:
            command.load()
            for handler in command.handlers:
                application.add_handler(handler)

    jobManager.init(application.job_queue)
    alarmJobManager.init(application.job_queue)

    application.run_polling()
