import sys
import socket
import threading
from threading import *

HOST = 'localhost'
PORT = 12345
users = {"jasmine": "codingGod", "maya":"guru", "chad":"chad", "carli":"g", "scarlett":"codingMaster", "hay": "student"}

threading = []
tid = 0

data_file_path = "."

# Declare a global variable to indicate whether the server should continue running
server_is_running = True

def handle_client(conn, addr):
    global server_is_running
    print(f"Accepted connection from {addr}")
    with conn:
        while server_is_running:
            conn, addr = s.accept()

            
            

            # Verifies the credentials
            if verify_credentials(username, password):
                print(f"Authenticated user {username} connected.")
            else:
                print(f"Failed authentication attempt from {addr}.")
                continue

            data = conn.recv(1024)
            username, password = data.decode().split(":", 1)
            if not data:
                break
            
            # Decode bytes to utf-8
            decoded_data = data.decode('utf-8').rstrip('\n')
            print(decoded_data)
            
            if decoded_data == "z":
                
                conn.close()  # Correctly close the current connection
                print("Gracefully shutting down the server")
                server_is_running = False  # Set the flag to stop the server
                sys.exit(0)
                break   # Break out of the loop to stop processing further requests
            
            # Echo the received data back to the client
            conn.sendall(data)


        # Closing the connection with the client
        print(f"Connection closed with {addr}")
        conn.close()
        sys.exit(0)


def verify_credentials(username, password):
    return users.get(username) == password

def run_server():
    global conn_id
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print("Server is ready to accept connections.")

        while server_is_running:  # Check the flag before accepting new connections
            # Accept incoming connections
            conn, addr = s.accept()
            conn_id += 1
            worker_thread = threading.Thread(target=worker())
            worker_thread.start()
            
            username = conn.recv(1024).decode('utf-8')
            password = conn.recv(1024).decode('utf-8')
            
            # Handle client communication in a dedicated thread
            #Thread[conn_id] = Thread(target=handle_client, args=(conn_id, conn, addr))
        
        s.close()
        sys.exit(0)

def worker():
    # Functionality goes here.
    Thread(target=handle_client, args=(conn_id, conn, addr))
    client_thread = Thread(target=handle_client, args=(conn_id, conn, addr))
    threading.append(client_thread)
    client_thread.start()

class CustomThread(threading.Thread):
    def __init__(self, tid, *args, **kwargs):
        self.tid = tid  # Set the thread ID
        super().__init__(*args, **kwargs)

    def run(self):
        print(f"Started thread {self.tid}")
        # Your desired functionality goes here.


run_server()