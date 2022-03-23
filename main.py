from twitchio.ext import commands
import os

bot = commands.Bot(prefix='?', initial_channels=['channel_name'], token='token')

#if you use folders to manage your files
for filename in os.listdir('./extensions'):
    if filename.endswith('.py'):
        bot.load_module(f'extensions.{filename[:-3]}')
        print(f'Loaded {filename} Successful')

if __name__ == '__main__':
    bot.run()
