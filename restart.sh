#!/bin/bash

BOT_SCRIPT="path-to-main.py" # Example: /home/ubuntu/discord-bot/main.py
SESSION_NAME="discord-bot"

screen -S $SESSION_NAME -X quit

screen -dmS $SESSION_NAME bash -c "python3 $BOT_SCRIPT"

sleep 2

BOT_PID=$(pgrep -f "$BOT_SCRIPT")

echo "PID Discord Bot: $BOT_PID"

sudo renice -20 -p $BOT_PID

ps -o pid,nice,comm -p $BOT_PID

exit 0
