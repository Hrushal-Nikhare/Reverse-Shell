import socket
import os


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
    # Set the IP address and port you want to check
    # add listing
    IP = "127.0.0.1"
    PORT = 105

    connection = connect(IP, PORT)
    if connection:
        # print("Connection successful.")
        os.system(f"start nc -l -p {PORT}") # Connect to reverse shell
    else:
        # print("Connection failed.")
        pass
    
