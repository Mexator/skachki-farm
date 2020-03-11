from telethon import TelegramClient
import asyncio
import time
api_id = 123
api_hash = 'XXX'
client = TelegramClient('session_name', api_id, api_hash)
client.start()
async def main():
    while True:
        entity = await client.get_entity('https://t.me/Horse_run_bot')
        await client.send_message(entity=entity,message='/bonus')
        print('Message was sent')
        time.sleep(60*60/2)
asyncio.get_event_loop().run_until_complete(main())
