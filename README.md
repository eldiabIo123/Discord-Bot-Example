# Discord Bot

A modular Discord bot built with nextcord.py.

## 📋 Requirements

- Ubuntu Server (tested on Ubuntu 20.04/22.04)
- Python 3.8+
- pip (Python package manager)

## 🚀 Installation

### 1. Update system packages
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install screen, Python and pip
```bash
sudo apt install python3 python3-pip screen -y
```

### 3. Configure pip (optional but recommended)
This allows installing packages system-wide without warnings:
```bash
mkdir -p $HOME/.config/pip && echo "[global]" > $HOME/.config/pip/pip.conf && echo "break-system-packages = true" >> $HOME/.config/pip/pip.conf
```

### 4. Install required Python packages
```bash
pip install nextcord pytz python-dotenv
```

### 5. Install optional packages
```bash
pip install dhooks
```

## 🔧 Configuration

### 1. Create a .env file in the bot directory:
```bash
nano .env
```

### 2. Add your bot token:
```text
TOKEN=your_bot_token_here
```

## 🎮 Running the Bot

### Method 1: Direct Python execution
```bash
python3 main.py
```

### Method 2: Using restart script
```bash
chmod +x ./restart.sh
./restart.sh
```

## ⚙️ Running as a Service (Autostart on boot)
To run the bot continuously in the background and automatically start on system boot:

### 1. Create a systemd service file:
```bash
sudo nano /etc/systemd/system/discord-bot.service
```

### 2. Paste the following configuration:
```ini
[Unit]
Description=Discord Bot Service
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/discord-bot
ExecStart=/bin/bash -c "sh ~/discord-bot/restart.sh"
ExecStop=/bin/bash -c "sh ~/discord-bot/stop.sh"
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### 3. Enable and start the service:
```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable autostart on boot
sudo systemctl enable discord-bot

# Start the bot
sudo systemctl start discord-bot

# Check status
sudo systemctl status discord-bot

# View logs
sudo journalctl -u discord-bot -f
```

### 4. Other Service Management Commands:
```bash
# Stop the bot
sudo systemctl stop discord-bot

# Restart the bot
sudo systemctl restart discord-bot

# Disable autostart
sudo systemctl disable discord-bot
```

## 📁 Project Structure
```bash
discord-bot/
├── main.py           # Main bot file
├── functions/        # Helper functions
├── modules/          # Bot modules/cogs
├── restart.sh        # Restart script
├── stop.sh          # Stop script
└── .env             # Environment variables (token)
```

## 🐛 Troubleshooting
```bash
# Check Python version
python3 --version

# Verify installed packages
pip list | grep nextcord

# Check service logs
sudo journalctl -u discord-bot -n 50 --no-pager

# Check if token is set correctly
cat .env

# U can check the logs when discord bot is running by this command (after -r is session_name)
screen -r discord-bot
```



