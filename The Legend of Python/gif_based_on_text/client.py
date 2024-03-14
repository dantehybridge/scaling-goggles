import os, random, discord
import get_gif as gg

def choose_word_from_words(words):
    return random.choice(words)
class Client(discord.Client):
    async def on_ready(self):
        print(f'You are successfully logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content:
            await self.send_gif(message)

    async def send_gif(self, message):
        chosen_word = choose_word_from_words(message.content.split())
        gifs = gg.get(chosen_word)
        
        if not gifs:
            print(f"No gifs found for word: {chosen_word}")
            return
        
        chosen_gif = random.choice(gifs['data'])['images']
        await message.channel.send(chosen_gif['original']['url'])    

discord_bot_api_key = os.getenv('DISCORD_BOT_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(discord_bot_api_key)