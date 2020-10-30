import re
import os
import sys
from colorama import Fore,init
import time
try:

    from pythonping import ping
except ModuleNotFoundError:

    os.system('pip install pythonping')
    from pythonping import ping


init(convert = True)

def pinger():
    the_ping = str(ping('8.8.8.8',count = 1))
    result = str(re.findall(r'Round Trip Times min/avg/max is (.*\d) ms',the_ping))
    final_result = re.findall(r'\s*\d*\.\d*',result)
    final_result = list(map(lambda x:float(x),final_result ))
    try:
        return final_result[1]
    except IndexError:
        return False  

def show_ping(number):
    if number == False:
        print(Fore.RED +'Lost Connection')

    elif number <=50:
        print(Fore.GREEN + str(number)+' ms')

    elif number > 50 or number <= 80:
        print(Fore.YELLOW + str(number)+' ms')

    elif number >= 81:

        print(Fore.RED + str(number)+' ms')
while True:

    try:

        number = pinger()
        show_ping(number)
        time.sleep(0.25)
        os.system("cls")
    except KeyboardInterrupt:
        print(Fore.WHITE + 'Goodbye')
        sys.exit()