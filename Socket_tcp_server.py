import socket
import time
import multiprocessing


def start_tcp_server():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    s.bind(('localhost', 443))

    # Listen for incoming connections(max of 5)
    s.listen(5)
    print("Server is listening...")

    # Establish a connection with the client
    c, addr = s.accept()
    print(f"Got connection from {addr}")

    while True:
        # Receive data from the client
        client_message = c.recv(1024).decode()
        if not client_message:
            break
        print(f"Received message from client: {client_message}")

        # Send a response to the client
        c.send(f'Received your message: {client_message}'.encode())
    c.close()


def start_tcp_client():
    time.sleep(2)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 443))

    for i in range(5):
        s.send(f'Hello from client {i}'.encode())

        print(s.recv(1024).decode())
        time.sleep(1)

    s.close()


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=start_tcp_server)
    client_process = multiprocessing.Process(target=start_tcp_client)
    server_process.start()
    client_process.start()
