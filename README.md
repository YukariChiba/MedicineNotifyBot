# MedicineNotifyBot
提醒您按时吃药的 Telegram Bot。

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
yarn
node index.js
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
      - BOT_TOKEN=[REDACTED]
    restart: always
    network_mode: 'host'
```

### Telegram

- `/create` to create a schedule.(Optional)
- `/subscribe [UUID]` to subscribe to a schedule.

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

## Command Module Format

```js
function Command(ctx) {
    // do something...
}

export default [
  {
    cmd: "[Your command]",
    cb: Command,
  },
];
```