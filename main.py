import discord
import os
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    allowed_extensions = ['.mp3', '.wav', '.m4a', '.ogg']
    folder_map = {
        '.mp3': 'MP3s',
        '.wav': 'WAVs',
        '.ogg': 'OGGs',
        '.m4a': 'M4As'
    }
    
    for attachment in message.attachments:
        ext = os.path.splitext(attachment.filename)[1].lower()
        if ext in allowed_extensions:
            folder_name = folder_map[ext]
            path = f"./downloads/{folder_name}/{attachment.filename}"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            await attachment.save(path)
            print(f"Downloaded {attachment.filename} to {path}")
            
        else:
            print(f"{attachment.filename} is not a valid file type!")
            
def run():
    client.run('INSERT BOT TOKEN') #insert your bot token here

if __name__ == "__main__":
    run()