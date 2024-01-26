import toml
from datetime import datetime
from colorama import Fore, Back, Style, init
import os
import platform
import psutil
import webbrowser as wb
import requests

init(autoreset=True)


now = datetime.now()

yıl = now.year
ay = now.month
gün = now.day
saat = now.hour
dakika = now.minute

response = requests.get('https://ipinfo.io')
data = response.json()

city = data.get('city', '')
country = data.get('country', '')
loc = data.get('loc', '').split(',')


if loc:
    latitude, longitude = loc
    



osname = os.name
if osname == 'nt':
    osname = 'Windows'
elif osname == 'posix':
    osname = 'Linux'
else:
    osname = 'unknown'

osversion = os.sys.platform

username = os.environ['USERNAME']

cpu = platform.processor()

disk = str(psutil.disk_usage('/').total / (1024 ** 3))

net_speed = str(psutil.net_if_stats()['Ethernet'].speed)

ram = str(psutil.virtual_memory().total / (1024 ** 3))
print(Fore.GREEN + 'OS: '+osname + '\n' + 'version: '+osversion + '\n' + 'running on: '+username + '\n'+ 'processor: '+cpu+ '\n' + 'disk: '+disk+' GB'+ '\n' + 'net speed: '+net_speed+'MB/S'+'\n' + 'RAM: '+ram+'MB \n')
print(Fore.RED+'DO NOT CHANGE THE .toml FILES!')

print(Fore.BLUE+f"{yıl}/{ay}/{gün} {saat}:{dakika}\n"+Style.RESET_ALL)

time = {
    'time': [
        {'time': f'{yıl}/{ay}/{gün}  {saat}:{dakika}', 'location': f'{country}, {city}', 'latitude': f'{latitude}', 'longitude': f'{longitude}'},
    ]
}

name = input(Fore.GREEN+'name: '+Fore.RED)

passwd = input(Fore.GREEN+'password: '+Fore.RED)
print('\n')



with open('toml/stock_info.toml', 'r', encoding='utf-8') as checkLogin:
    stock_info = toml.load(checkLogin)

if name == stock_info['login_name'][0]['name'] and stock_info['login_passwd'][0]['passwd'] == passwd:
    with open('toml/login_times.toml', 'a', encoding='utf-8') as saveTime:
        toml.dump(time, saveTime)
    os.chdir('directory')
    print(Fore.GREEN+'login success! \nby aalper16\n')
    print(Fore.BLUE+"type 'help' or '?' to see the commands")
    while True:
        command = input(Fore.RED+'command@'+username+'-'+name+': ')
        if command == 'new_txt':
            name_txt = input('file name: ')
            inside_txt = input('file: ')
            text = {
                'texts': [
                    {'name': f'{name_txt}', 'file': f'{inside_txt}'}
                ]
            }
            with open('toml/user_texts.toml', 'a', encoding='utf-8') as saveText:
                toml.dump(text, saveText)
        elif command == 'read_txt':
            line = int(input('line number: '))
                
            with open('toml/user_texts.toml', 'r', encoding='utf-8') as readText:
                all_texts = toml.load(readText)
                    
            if line < len(all_texts['texts']):
                textRead = all_texts['texts'][line]
                print(textRead)
            else:
                print("no lines.")

        elif command == 'web':
            browser_link = input('link: ')
            wb.open(browser_link)
            link = {
                'links': [
                    {'url': f'{browser_link}'}
                ]
            }
            with open('toml/opened_links.toml', 'a', encoding='utf-8') as openLink:
                toml.dump(link, openLink)

        elif command == 'change_login':
            new_name = input('new name: ')
            new_passwd = input('new password: ')
            new_passwd_confirm = input('confirm new password: ')

            if new_passwd == new_passwd_confirm:
                try:
                    infos = {
                        'login_name': [
                            {'name': f'{new_name}'}
                        ],
                        'login_passwd': [
                            {'passwd': f'{new_passwd}'}
                        ]
                    }
                    with open('toml/stock_info.toml', 'w', encoding='utf-8') as changeLogin:
                        toml.dump(infos, changeLogin)

                    print('changed login successfully'+Style.RESET_ALL)
                except:
                    print("error: can't save changes"+Style.RESET_ALL)
            else:
                print('2 passwords should be the same')
        elif command == 'clear':
            os.system('cls')

        elif command == 'time':
            print(f"{yıl}/{ay}/{gün} {saat}:{dakika}\n")

        elif command == 'getcwd':
            print(os.getcwd())

        elif command == 'cd':
            directory = input('directory: ')
            os.chdir(directory)

        elif command == 'mkdir':
            file_name = input('file name: ')
            try:
                os.mkdir(file_name)
                print('success!')
            except FileExistsError:
                continue
                print('already exists')

        elif command == 'mkfile':
            doc_name = input('document name: ')
            with open(doc_name, 'w') as newFile:
                print('success!')

        elif command == 'ls':
            os.system('dir')

        elif command == 'logout':
            print('logged out')
            break

        elif command == 'sysinfo':
            from sysinfo import *
            all()

        elif command == 'nano':
            doc_name2 = input('document name: ')
            doc = input('document: ')
            doc_bytes = doc.encode('utf-8')
            print(os.system('type '+doc_name))
            with open(doc_name2, 'a') as writeInto:
                writeInto.write(doc)

        elif command == 'cat':
            doc_name = input('document name: ')
            print(os.system('type '+doc_name))

        elif command == 'rm':
            doc_name3 = input('document name: ')
            size = os.path.getsize(doc_name3)
            sure = input(str(size)+' KB of disk space will be freed. y/n? ')
            if sure == 'y' or sure == 'Y':
                os.remove(doc_name3)
            elif sure == 'n' or sure == 'N':
                continue
            else:
                print('not a parameter!')

        elif command == 'help' or command == '?':
            print("""
                  
    new_txt: creates a new text file
    read_txt: reads the txt files
    web: starts a webpage by URL
    change_login: changes the username and password
    sysinfo: gives the system info
    logout: logs out the terminal
    cat: shows what's inside in a document
    ls: shows the directory
    rm: deletes directory or document
    mkdir: creates a directory
    mkfile: creates a file
    nano: writes into a document (like .txt)
                  
""")    
        elif command == 'exit':
            print('logging out...')
            break    
        
        else:
            print('not a command!')
else:
    print('login failed!')


