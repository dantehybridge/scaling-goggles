import random, discord
import get_gif as gg

api_key = '' # Replace with your own API key.

def choose_word_from_words(words):
    return random.choice(words)

class Client(discord.Client):
    async def on_ready(self):
        print(f'You are successfully logged in as {self.user}')
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content != '':
            chosen_word = choose_word_from_words(message.content.split())
            gifs = gg.get(chosen_word)
            chosen_gif = random.choice(gifs['data'])['images']
            await message.channel.send(chosen_gif['original']['url'])

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(api_key)