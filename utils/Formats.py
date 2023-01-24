from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def formatDrugs(drugs):
    return '\n'.join([
        f'{drug["name"]}: {drug["amount"]}' + (f'\n_\({drug["desc"]}\)_' if "desc" in drug else '') for drug in drugs
    ])


def formatNotify(itv):
    return '*该吃药了！*\n' + formatDrugs(itv["contents"])


def formatAlarm(itv, cnt):
    if cnt == 6:
        return f'*该吃药了！*_\(最终提醒\)_\n' + formatDrugs(itv["contents"])
    return f'*该吃药了！*_\(第{cnt}次提醒\)_\n' + formatDrugs(itv["contents"])


def formatIntervals(itvs):
    return '\n'.join([
        '\-\-\-\-\-\-\-\-\n' + f'时间段 {idx}：`{itv["interval"]}`\n' + formatDrugs(itv["contents"]) for idx, itv in enumerate(itvs)
    ])


def formatSchedule(schedule):
    return f'*{schedule["title"]}*\n订阅人数：{len(schedule["subscribers"])}\n' + formatIntervals(schedule["details"])


def formatSuppressKeyboard(alarmid):
    keyboard = [
        [
            InlineKeyboardButton(
                "标记完成，此次不再提醒", callback_data=f'suppress {alarmid}'),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
