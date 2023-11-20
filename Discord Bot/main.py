import os, random, re, discord
# from dotenv import load_dotenv

# load_dotenv()
f = open("C:\\Users\\shado\Desktop\\Stonks\\Discord Bot\\secret", "r")
TOKEN = f.readline()
f.close()

customIntents=discord.Intents.default()
customIntents.guild_messages = True
customIntents.messages = True
customIntents.message_content = True 

client = discord.Client(intents = customIntents)

class bot:
    def __init__(self):
        self.responses = []
        self.id = 1234
        
    def add_response(self, response):
        self.responses.append(response)

    def returnMessage(self, message):
        return message
        
    def respond(self, message):
        for response in self.responses:
            for trigger in response.triggers:
                if(re.search(trigger, message.content.lower())):
                    return response.response

class Response:
    def __init__(self, response, *triggers):
        self.triggers = []
        self.response = response
        for trigger in triggers:
            self.triggers.append(trigger)

BOT = bot()
BOT.add_response(Response("???", "ANSWERS", "ANSWERS"))

@client.event
async def on_message(message):
    realContent = message.content
    lowerContent = message.content.lower()
    lowerTokenized = lowerContent.split(' ')
    response = ""
    
    if message.author == client.user:
        return

    if lowerTokenized[0] == "s!" and lowerTokenized[1] == "daily":
        print("This is your daily stock info")
    # elif "where is" in lowerContent or "where\'s" in lowerContent or "wheres" in lowerContent:

print("Bot Started")
client.run(TOKEN)