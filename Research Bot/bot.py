import os, random, re, discord, time
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'NDIyOTUwMDI3MjA4NTU2NTQ1.GrOLDl.WxOlIce8QGf_MCExcl5Bl9C9hdVcjmLIXgaFno'
#GUILD = os.getenv('DISCORD_GUILD')

simpleKeyWords = []

customIntents=discord.Intents.default()
customIntents.guild_messages = True
customIntents.messages = True
customIntents.message_content = True 
client = discord.Client(intents = customIntents)

class bot:
    def __init__(self):
        self.responses = []
        self.id = 1234
        self.message = ""
        
    def add_response(self, response):
        self.responses.append(response)
        
    def respond(self):
        for response in self.responses:
            for trigger in response.triggers:
                if(re.search(trigger, self.message.content.lower())):
                    return response.response

class Response:
    def __init__(self, response, *triggers):
        self.triggers = []
        self.response = response
        for trigger in triggers:
            self.triggers.append(trigger)
            simpleKeyWords.append(trigger)

stockbot = bot()

@client.event
async def on_message(message):
    stockbot.message = message
    realContent = message.content
    lowerContent = message.content.lower()
    response = ""
    target = ""
    
    #print(message)

    #stockbot.add_response(Response(RESPONSE, TRIGGER, TRIGGER, ...))
    stockbot.add_response(Response("Beg my little baby", "please"))

    if message.author == client.user:
        return

    # elif "where is" in lowerContent or "where\'s" in lowerContent or "wheres" in lowerContent:
    
    elif any(ext in lowerContent for ext in simpleKeyWords):
        msg = stockbot.respond()
        await message.channel.send(msg)

print("Bot Started")
client.run(TOKEN)