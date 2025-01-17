# WOOF Spot-to-PoolX Notifier  

This Python script monitors the amount of `$WOOF` tokens available on your Bitget spot account. If the token count exceeds a defined threshold, the script sends a notification to a Telegram chat with a link to PoolX, encouraging you to deposit the tokens into the pool.  

## Features  
- Fetches `$WOOF` balance from your Bitget account.  
- Notifies a Telegram chat when the `$WOOF` count reaches or exceeds a predefined threshold.  
- Provides a customizable threshold and message template.  

## Prerequisites  

- **Python version**: 3.6+  
- **Required Libraries**:  
  Install the following libraries if not already installed:  
  ```bash
  pip install requests
  ```  

## Installation  

1. Clone the repository:  
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```  

2. Set up the `config.py` file:  
   Create a `config.py` file in the root directory and define the following variables:  
   ```python
   passphrase = "<your_bitget_passphrase>"
   api_key = "<your_bitget_api_key>"
   secret_key = "<your_bitget_secret_key>"
   WOOF_COUNT_TO_INFORM = 100  # Replace with your threshold value
   CHAT_ID = "<your_telegram_chat_id>"
   BOT_API = "<your_telegram_bot_api_key>"
   POOLX_URL = "<your_poolx_url>"
   ```  

3. Run the script:  
   ```bash
   python main.py
   ```  

## Files Overview  

- **`main.py`**: The main entry point of the script. It fetches the `$WOOF` balance and sends notifications as needed.  
- **`config.py`**: Stores configuration values such as API keys, thresholds, and URLs.  
- **`woof.py`**: Contains the `get_available_coins(client)` function to fetch the `$WOOF` balance.  
- **`send_message.py`**: Provides the `send_message(bot_api, chat_id, msg)` function to send Telegram notifications.  

## Usage  

1. The script connects to your Bitget account using the credentials in `config.py`.  
2. It checks the `$WOOF` token balance on your spot wallet.  
3. If the token count meets or exceeds `WOOF_COUNT_TO_INFORM`, a message with the PoolX link is sent to your Telegram chat. Otherwise, a message with the current `$WOOF` balance is sent.  

### Example Output  

#### When threshold is met:  
```
🤑 На споте 120.00 $WOOF.

❤️‍🔥 Пора бы им в PoolX  

<POOLX_URL>
```  

#### When below threshold:  
```
Количество $WOOF на споте: 80.00
```  

## Contributing  

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.  


---  

Happy automating! 🚀  
```
