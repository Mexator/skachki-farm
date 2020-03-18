# skachki-farm
Script for sending messages to Skachki Telegram bot to farm money

## Running
1. Substitute api_id and api_hash to your own ones in ```main.py``` file.
    You can obtain them on [my.telegram.org](https://my.telegram.org/)->API development tools
2. Run ```python3 main.py --bootstrap```
    This command will create a session file, needed to identify user,
    that sends message 
3. Run ```docker build -t container_name```
4. Run ```docker run -it container_name``` 
