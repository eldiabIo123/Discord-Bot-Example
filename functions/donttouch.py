#########################################################
### IMPORTS                                           ###
#########################################################
import os
from functions.time import Date
from functions.colors import Color

#########################################################
### Class                                             ###
#########################################################
class Modules:
    def load(self, client, folder: str, path: str):
        for file in os.listdir(str(path + '/' + folder)):
            if file.endswith('.py'):
                try:
                    client.load_extension(f'{folder}.{str(file)[:-3]}')
                    print(f'{Color.GRAY}[{Color.GREEN}+{Color.GRAY}]{Color.WHITE} Loaded {file[:-3]}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')
                except Exception as err:
                    print(f'{Color.GRAY}[{Color.RED}#{Color.GRAY}]{Color.WHITE} Error loading {file[:-3]}: {Color.RED}{err}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')
    
    def enable(self, client, module: str, folder: str):
        client.load_extension(f"{folder}.{module}")
        print(f'{Color.GRAY}[{Color.GREEN}+{Color.GRAY}]{Color.WHITE} Loaded module {module}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')

    def disable(self, client, module: str, folder: str):
        client.unload_extension(f"{folder}.{module}")
        print(f'{Color.GRAY}[{Color.RED}-{Color.GRAY}]{Color.WHITE} Unloaded module {module}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')

    def reload(self, client, module: str, folder: str):
        client.reload_extension(f"{folder}.{module}")
        print(f'{Color.GRAY}[{Color.YELLOW}*{Color.GRAY}]{Color.WHITE} Reloaded module {module}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')

    def reload_all(self, client, folder: str, path: str):
        for file in os.listdir(str(path + '/' + folder)):
            if file.endswith('.py'):
                try:
                    client.reload_extension(f'{folder}.{str(file)[:-3]}')
                    print(f'{Color.GRAY}[{Color.YELLOW}*{Color.GRAY}]{Color.WHITE} Reloaded module {file[:-3]}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')
                except Exception as err:
                    print(f'{Color.GRAY}[{Color.RED}#{Color.GRAY}]{Color.WHITE} Error reloading {file[:-3]}: {Color.RED}{err}  {Color.CYAN}/ {Color.WHITE}{Date().now("%H:%M:%S %d-%m-%Y")}{Color.RESET}')