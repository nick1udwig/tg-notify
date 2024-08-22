# tg-notify

Send yourself a Telegram message to notify you when a long-running command has finished:
```
./my_long_running_command && tg-notify.py
```

## Setup

```
# Clone this repo
git clone git@github.com:nick1udwig/tg-notify.git

# Create a TG bot
https://core.telegram.org/bots/tutorial#obtain-your-bot-token

# Copy the bot token/API key from above into `my_api_key.txt`:
cd tg-notify
cat <YOUR_BOT_TOKEN> > my_api_key.txt

# Get your chat ID
## Start a chat with the bot in your Telegram client
## Send a message to the bot
## Run:
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
## Send another message to the bot
## Run again:
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

# Copy the `result.chat.id` field from above into `my_chat_id.txt:
cat <CHAT_ID> > my_chat_id.txt
```
