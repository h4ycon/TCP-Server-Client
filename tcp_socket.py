import socket

from threading import Thread

HOST = 'localhost'
PORT = 12345

def handle_client(conn, addr):
    print(f"Accepted connection from {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            # Echo the received data back to the client
            conn.sendall(data)

    print(f"Connection closed with {addr}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is ready to accept connections.")
    
    while True:
        # Accept incoming connections
        conn, addr = s.accept()
        
        # Handle client communication in a dedicated thread
        client_thread = Thread(target=handle_client, args=(conn, addr))
        client_thread.start()



