import socket
import time
import multiprocessing


def start_udp_server():
    # Create a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    s.bind(('localhost', 443))
    print("Server is listening...")

    while True:
        # Receive client_message from the client
        client_message, addr = s.recvfrom(1024)
        print(
            f"Received message from client {addr}: {client_message.decode()}")

        # Send a response to the client
        s.sendto(
            f'Received your message: {client_message.decode()}'.encode(), addr)


def start_udp_client():
    time.sleep(2)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 443)

    for i in range(5):
        s.sendto(f'Hello from client {i}'.encode(), server_address)

        server_response, _ = s.recvfrom(1024)
        print(server_response.decode())
        time.sleep(2)

    s.close()


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=start_udp_server)
    client_process = multiprocessing.Process(target=start_udp_client)
    server_process.start()
    client_process.start()
