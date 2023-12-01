# Python Reverse Shell

## Requirements

- Windows 10
- Python 3
- Internet
- Both devices should be connected to same network

## Usage

- Run `webserver.py` on the head device (This will be used to serve files for `Installer.py`)

- Run `Installer.py` (In files folder) on the target device (This will install the required files on the target device along with a game as distraction)

- Run `Interface.py` to connect to the target device (This will connect to the target device and will give you a shell)

## Features

- cmd reverse shell

- persistent across reboots

## Drawbacks

- Does not immediately start when infected (have to wait for a reboot)

- Must exit shell with `exit` command (Otherwise it will jam the socket connection)

## How it works

- `Installer.py`
    - Creates a folder in AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    - Copies the files from files folder to the created folder
    - Creates a shortcut to the game in the created folder
    - Runs the game as a distraction
    
- `Interface.py`
    - Connects to the target device
    - Sends commands to the target device
    - Receives output from the target device using the standard library `sockets`

- `webserver.py`
    - Serves the files for `Installer.py`
    - Logs the Ip address of the target device for use in `Interface.py`

- `Reverse.py`
    - Runs on the target device
    - Creates a socket connection to the head device
    - Executes commands from the head device
    - Sends output to the head device
    - Runs in a loop

## Disclaimer

I am not responsible for any damage caused by this program. This is for educational purposes only.

## License

[MIT](https://choosealicense.com/licenses/mit/)
