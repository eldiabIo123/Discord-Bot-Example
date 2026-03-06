#########################################################
### IMPORTS                                           ###
#########################################################
import os
import nextcord
from dotenv import load_dotenv
from functions.time import Date
from nextcord.ext import commands
import functions.donttouch as eld
from functions.colors import Color

#########################################################
### VARIABLES                                         ###
#########################################################
load_dotenv()
intents = nextcord.Intents.all()
intents.members = True
intents.messages = True
intents.message_content = True

bot_name = ""

client = commands.Bot(intents=intents)
admins = [] # Put your user ID in this table

clean_start = True
#########################################################
### Events                                            ###
#########################################################
@client.event
async def on_ready():
    global clean_start
    print(f"{Color.GRAY}[{Color.GREEN}READY{Color.GRAY}]{Color.WHITE} {bot_name} is ready to work.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")
    if clean_start:
        clean_start = False
        await client.sync_all_application_commands()
        print(f"{Color.GRAY}[{Color.BLUE}INFO{Color.GRAY}]{Color.WHITE} Commands have been synchronized.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")

@client.event
async def on_connect():
    print(f"{Color.GRAY}[{Color.GREEN}ONLINE{Color.GRAY}]{Color.WHITE} {bot_name} has internet access.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")

@client.event
async def on_resumed():
    print(f"{Color.GRAY}[{Color.GREEN}ONLINE{Color.GRAY}]{Color.WHITE} {bot_name} has internet access.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")

@client.event
async def on_disconnect():
    print(f"{Color.GRAY}[{Color.RED}OFFLINE{Color.GRAY}]{Color.WHITE} {bot_name} has been disconnected from the internet.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")

#########################################################
### Reload command                                    ###
#########################################################
@client.slash_command(name="reload", description="Manages modules.")
async def reload(interaction: nextcord.Interaction, action: str = nextcord.SlashOption(description='What do you want to do?', choices={"Reload": "reload", "Enable": "enable", "Disable": "disable"}, required=True), module: str = nextcord.SlashOption(description='Enter the module name', required=False)):
    try:
        if interaction.user:
            if interaction.user.id in admins:
                if module is not None:
                    if action == "enable":
                        eld.Modules().enable(client, module=module, folder="modules")
                        await interaction.response.send_message(embed=nextcord.Embed(title=f"Module {module} has been enabled.", color=0x00FF00), ephemeral=True)
                    elif action == "disable":
                        eld.Modules().disable(client, module=module, folder="modules")
                        await interaction.response.send_message(embed=nextcord.Embed(title=f"Module {module} has been disabled.", color=0x00FF00), ephemeral=True)
                    elif action == "reload":
                        eld.Modules().reload(client, module=module, folder="modules")
                        await interaction.response.send_message(embed=nextcord.Embed(title=f"Module {module} has been reloaded.", color=0x00FF00), ephemeral=True)
                else:
                    if action == "reload" or action is None:
                        eld.Modules().reload_all(client, folder='modules', path=f"{str(os.path.dirname(os.path.abspath(__file__)))}")
                        await interaction.response.send_message(embed=nextcord.Embed(title='All modules have been reloaded.', color=0x00FF00), ephemeral=True)
                    else:
                        await interaction.response.send_message(embed=nextcord.Embed(title='Cannot enable or disable all modules.', color=0xFF0000), ephemeral=True)
            else:
                await interaction.response.send_message(embed=nextcord.Embed(title='🛡️ Insufficient permissions.', color=0xFF0000), ephemeral=True)

    except commands.ExtensionNotFound:
        await interaction.response.send_message(embed=nextcord.Embed(title='Module not found.', color=0xFF0000), ephemeral=True)
    except commands.ExtensionNotLoaded:
        await interaction.response.send_message(embed=nextcord.Embed(title='Module is not loaded.', color=0xFF0000), ephemeral=True)
    except commands.ExtensionAlreadyLoaded:
        await interaction.response.send_message(embed=nextcord.Embed(title='Module is already loaded.', color=0xFFFF00), ephemeral=True)
    except commands.ExtensionFailed as err:
        await interaction.response.send_message(embed=nextcord.Embed(title='Module exists but cannot be loaded (error in file).', description=str(err), color=0xFF0000), ephemeral=True)
    except Exception as err:
        print(f"{Color.GRAY}[{Color.RED}ERROR{Color.GRAY}]{Color.WHITE} Error while executing /reload command:{Color.RED} {err}.{Color.RESET}")
        await interaction.response.send_message(embed=nextcord.Embed(title='An unknown error occurred.', description=str(err), color=0xFF0000), ephemeral=True)

#########################################################
### BOT STARTUP                                       ###
#########################################################
def start():
    global bot_name
    if bot_name == "":
        bot_name = "Discord Bot"
    print(f"{Color.GRAY}[{Color.BLUE}INFO{Color.GRAY}]{Color.WHITE} Starting {bot_name} startup procedure.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")
    print(f"{Color.GRAY}[{Color.BLUE}INFO{Color.GRAY}]{Color.WHITE} Starting to load modules.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")
    print(f"{Color.GRAY}========================================================================{Color.RESET}")
    eld.Modules().load(client, folder='modules', path=f"{str(os.path.dirname(os.path.abspath(__file__)))}")
    print(f"{Color.GRAY}========================================================================{Color.RESET}")
    print(f"{Color.GRAY}[{Color.BLUE}INFO{Color.GRAY}]{Color.WHITE} Module loading completed.  {Color.CYAN}/ {Color.WHITE}{Date().now('%H:%M:%S %d-%m-%Y')}{Color.RESET}")
    client.run(str(os.getenv('TOKEN')))

start()