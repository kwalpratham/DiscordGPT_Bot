import discord
from dotenv import load_dotenv
import os
import openai

load_dotenv()

token = os.getenv("SECRET_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # print(message.text)
        if self.user != message.author and self.user in message.mentions:
            
            channel = message.channel
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.content,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
            messageToSend = response.choices[0].text
            print(message.author, message.mentions, message.channel)
            await channel.send("Hi this is your GPT Bot")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)