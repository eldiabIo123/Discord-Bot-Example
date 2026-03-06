#########################################################
### IMPORTS                                           ###
#########################################################
import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands, tasks

#########################################################
### Class                                             ###
#########################################################
class Example(commands.Cog):
    def __init__(self, client):
        load_dotenv("../.env") # For some API keys or passwords
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass
        # self.loop.start() 

    @tasks.loop(seconds=0.5)  
    async def loop(self):
        pass

    @nextcord.slash_command(name='hello', description='')
    async def command(self, interaction:nextcord.Interaction):
        await interaction.response.send_message("Hi")

#########################################################
### Function                                          ###
#########################################################
def setup(client):
    client.add_cog(Example(client))