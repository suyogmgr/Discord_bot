from typing import Final

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response


#loads the .env file on the current directory
load_dotenv()

Token: Final[str] = os.getenv("Discord_Token")

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

async def send_message(message: Message, usr_message: str) ->None:
    if not usr_message:
        print("Message is empty, something went wrong")
        return
     
    #walrus operator :=
    #if is_private := usr_message[0] == "?":
    
    is_private = usr_message[0] == "?"

    if is_private:
        usr_message == usr_message[1:]

    try:
        response: str = get_response(usr_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f"{client.user} us now running")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    

    username: str = str(message.author)
    usr_message: str = message.content
    channel: str = str(message.channel)


    print(f"[{channel}] {username} :'{usr_message}'")
    await send_message(message, usr_message)


def main() -> None:
    client.run(token=Token)


if __name__ == "__main__":
    main()