# MedicineNotifyBot

提醒您按时吃药的 Telegram Bot。（重制版）

## Features

- cron 提醒语法。
- 支持多个计划，多个时间安排。
- 支持随时订阅和取消订阅。
- （WIP）支持创建计划。
- （WIP）支持外部方案存储。
- （WIP）支持通过 GitHub Issue 创建外部方案。
- （WIP）方案分享。

## Usage

### Run

```bash
pip install -r requirements.txt
python main.py
```

### Docker

```yaml
version: "3"
services:
  medbot:
    image: ghcr.io/yukarichiba/medicinenotifybot:main
    container_name: medbot
    hostname: "medbot"
    volumes:
      - ./schedules:/code/schedules
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/HongKong
      - BOTTOKEN=[REDACTED]
    restart: always
    network_mode: 'host'
```

### Telegram

- `/create` to create a schedule. (WIP)
- `/subscribe [UUID]` to subscribe to a schedule.
- `/unsubscribe [UUID]` to unsubscribe to a schedule.
- `/info [UUID]` to preview a schedule.
- `/list` to get a list of subscribed schedules.

## Schedule Format

```json
{
    "title": "测试方案",
    "subscribers": [],
    "details": [
        {
            "interval": "0 12 * * *",
            "contents": [
                {
                    "name": "药丸",
                    "amount": "1粒",
                    "desc": "与肥宅快乐水一同服用。"
                },
                {
                    "name": "药片",
                    "amount": "1/2片"
                }
            ]
        },
        {
            "interval": "0 */8 * * *",
            "contents": [
                {
                    "name": "肥宅快乐水",
                    "amount": "1瓶",
                    "desc": "500 ml"
                }
            ]
        }
    ]
}
```