async def replyMarkdownMsg(update, context, msg, reply_markup=None):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=msg, parse_mode='MarkdownV2', reply_markup=reply_markup)


async def replyPlainMsg(update, context, msg, reply_markup=None):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=msg, reply_markup=reply_markup)


async def sendMarkdownMsg(context, chatid, msg, reply_markup=None):
    await context.bot.send_message(chat_id=chatid, text=msg, parse_mode='MarkdownV2', reply_markup=reply_markup)


async def sendPlainMsg(context, chatid, msg, reply_markup=None):
    await context.bot.send_message(chat_id=chatid, text=msg, reply_markup=reply_markup)
