from telethon import TelegramClient
import asyncio
import time
import sys
api_id = 123
api_hash = 'XXX'
client = TelegramClient('skacki_farm', api_id, api_hash)
client.start()
async def main():
    entity = await client.get_entity('https://t.me/Horse_run_bot')
    waiting_multiplier=1
    while True:
        try:
            await asyncio.wait_for(client.send_message(entity=entity,message='/bonus'),timeout=3.0)
            print('Message was sent')
            time.sleep(60*60)
            waiting_multiplier=1
        except asyncio.TimeoutError:
            print('Error sending message, retry in',10*waiting_multiplier,'seconds')
            await asyncio.sleep(10*waiting_multiplier)
            waiting_multiplier*=2
if len(sys.argv) > 1 and sys.argv[1] == "--bootstrap":
    sys.exit()
asyncio.get_event_loop().run_until_complete(main())
