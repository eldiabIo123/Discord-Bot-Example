#!/bin/bash

# Ścieżka do Twojego skryptu Discord bota
BOT_SCRIPT="/home/ubuntu/discord-bot/kamil-bot.py"
SESSION_NAME="kamil-bot"

screen -S $SESSION_NAME -X quit

# Utworzenie nowej sesji screen i uruchomienie bota
screen -dmS $SESSION_NAME bash -c "python3 $BOT_SCRIPT"

# Zaczekanie chwilę, aby proces bota się uruchomił
sleep 2

# Uzyskanie PID procesu uruchomionego w sesji screen
BOT_PID=$(pgrep -f "$BOT_SCRIPT")

# Debug: Wyświetlenie PID bota
echo "PID bota Discord: $BOT_PID"

# Ustawienie wartości nice na 15 dla procesu bota
sudo renice -20 -p $BOT_PID

# Debug: Sprawdzenie nowej wartości nice
ps -o pid,nice,comm -p $BOT_PID

# Zakończenie skryptu
exit 0
