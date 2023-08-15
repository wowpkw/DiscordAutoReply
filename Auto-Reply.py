import sys
sys.path.insert(0, 'discord.py-self')

from discord.ext import commands
import json
import socket 
from colorama import Fore
import os

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
masked_ip = '.'.join(['*'*len(octet) for octet in ip_address.split('.')])

with open('config1.json', 'r') as file:
    config = json.load(file)



token = config['token']
prefix = config['prefix']
owner_id = config['admin_id']
owner = config['admin_username']


me = f"<@{owner_id}>"


bot = commands.Bot(command_prefix=prefix)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()
print(Fore.MAGENTA + f'''
       ╔══════════════════════════════════════════════════════════════════════════════════════════════╗q
       ║██████╗░██╗░░██╗░██╗░░░░░░░██╗██╗░██████╗  ██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░║;
       ║██╔══██╗██║░██╔╝░██║░░██╗░░██║╚█║██╔════╝  ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗║;
       ║██████╔╝█████═╝░░╚██╗████╗██╔╝░╚╝╚█████╗░  ██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║║;
       ║██╔═══╝░██╔═██╗░░░████╔═████║░░░░░╚═══██╗  ██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║║;
       ║██║░░░░░██║░╚██╗░░╚██╔╝░╚██╔╝░░░░██████╔╝  ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝║;
       ║╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═════╝░  ╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░║;
       ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║;
       ║░█████╗░██╗░░░██╗████████╗░█████╗░░░░░░░██████╗░███████╗██████╗░██╗░░░░░██╗░░░██╗╔════════════╝;
       ║██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██╔════╝██╔══██╗██║░░░░░╚██╗░██╔╝║v------------J
       ║███████║██║░░░██║░░░██║░░░██║░░██║█████╗██████╔╝█████╗░░██████╔╝██║░░░░░░╚████╔╝░║;
       ║██╔══██║██║░░░██║░░░██║░░░██║░░██║╚════╝██╔══██╗██╔══╝░░██╔═══╝░██║░░░░░░░╚██╔╝░░║;
       ║██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝░░░░░░██║░░██║███████╗██║░░░░░███████╗░░░██║░░░║;
       ║╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚══════╝░░░╚═╝░░░║;
       ╚═════════════════════════════════════════════════════════════════════════════════╝J
      ''')
@bot.event
async def on_ready():
  print(Fore.MAGENTA + f'''
  » Logged in as:\r
  » User: ''' + Fore.GREEN + f'{bot.user.name}' + Fore.MAGENTA + ''' \r
  » ID: ''' + Fore.GREEN + f'{bot.user.id}' + Fore.MAGENTA + ''' \r
  » Admin: ''' + Fore.GREEN + f'{owner}' + Fore.MAGENTA + '''
  » Admin ID: ''' + Fore.GREEN + f'{owner_id}' + Fore.MAGENTA + '''
  » CONNECTED @ IP ; ''' + Fore.GREEN + f'{ip_address}' + Fore.MAGENTA + '''
        ''')
  print("-" * 35)
  print()
  print(Fore.GREEN + "  $" + Fore.WHITE + ' SUCCESS!')
  print(Fore.BLUE + "\n""  » BOT is " + Fore.GREEN + "online." + Fore.BLUE + "\n")


userid = input(Fore.GREEN + "$" + Fore.WHITE + " Enter the User ID ~ " + Fore.MAGENTA)
responsemsg = input(Fore.GREEN + "$" + Fore.WHITE + " Enter the auto-reply message ~ " + Fore.MAGENTA)

@bot.event
async def on_message(message):
    if str(message.author.id) == (str(userid)):
        await message.channel.send(responsemsg)
        await bot.process_commands(message)



bot.run(token)