import os

def index_files(directory):
    file_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
                file_dict[file] = content
    return file_dict

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
ips = f'{os.getcwd()}\\ips'
file_dict = index_files(ips)
# print(file_dict)

for item , value in file_dict.items():
    print(f'{item} : {value}')

selected = input('Select a ip: ')
clear()
print(f'You selected {selected}')
print(f'Connecting to {selected}')
