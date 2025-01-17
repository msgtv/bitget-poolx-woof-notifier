# Bitget PoolX Woof Notifier

## Overview
This script automates the process of monitoring the amount of $WOOF tokens on your Bitget spot account and sends notifications when the balance exceeds a specified threshold. The notification suggests transferring tokens to PoolX to benefit from compound interest.

## Features
- Monitors $WOOF token balance on your Bitget spot account.
- Sends Telegram notifications when the balance meets the configured threshold.

## Requirements
- Python 3.6+
- Virtual environment

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd bitget-poolx-woof-notifier
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys and Settings
Update the `config.py` file with the following information:
- `passphrase`: Your Bitget API passphrase.
- `api_key`: Your Bitget API key.
- `secret_key`: Your Bitget API secret key.
- `WOOF_COUNT_TO_INFORM`: The threshold for $WOOF token balance to trigger notifications.
- `CHAT_ID`: Your Telegram chat ID.
- `BOT_API`: Your Telegram bot API token.
- `POOLX_URL`: The URL for PoolX.

### 5. Test the Script
Run the script to ensure it works as expected:
```bash
.venv/bin/python main.py
```

### 6. Automate with Cron
To run the script every 2 minutes, follow these steps:

#### Open Crontab
```bash
crontab -e
```

#### Add Cron Job
```bash
*/2 * * * * /root/bitget-poolx-woof-notifier/.venv/bin/python /root/bitget-poolx-woof-notifier/main.py >> /root/bitget-poolx-woof-notifier/cron.log 2>&1
```

#### Save and Exit
- In `nano`, press `CTRL+O`, `Enter`, then `CTRL+X`.
- In `vim`, press `ESC`, type `:wq`, and press `Enter`.

#### Verify Cron Job
```bash
crontab -l
```
Ensure your cron job is listed.

#### Check Cron Status
Make sure the cron service is active:
```bash
systemctl status cron
```
If it is not running, start it:
```bash
systemctl start cron
systemctl enable cron
```

## Logging
To debug or verify execution, logs are written to `cron.log` in the project directory.

## Support
For any issues or feature requests, feel free to open an issue in the repository.

