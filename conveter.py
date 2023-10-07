# needed .bat file with py converter.py \n pause

from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession
import asyncio
import os
import shutil
import uuid
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

async def main(filename):
    try:
        client = TelegramClient(filename)
        tdesk = await client.ToTDesktop(flag=UseCurrentSession)

        basename = "tdata"
        hexed = str(uuid.uuid4())
        path = "_".join([basename, hexed])

        tdesk.SaveTData(os.path.join('tdatas', os.path.join(path.split('.')[0]), 'tdata'))
        print(Fore.GREEN + f'Сессия: {filename}' + Fore.RESET + Fore.GREEN + ' успешно сохранена в папку: ' + Fore.GREEN + f'{path}')
    except:
        print(Fore.RED + 'Ошибка')
        shutil.rmtree('tdatas/' + path)



for filename in os.listdir('sessions'):
    if filename.endswith(".session"):
        print(Fore.YELLOW + f'Обрабатывается: {filename}')
        asyncio.run(main(os.path.join('sessions', filename)))

