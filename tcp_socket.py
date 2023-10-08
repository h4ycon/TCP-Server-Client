import sys
import socket
from threading import Thread

HOST = 'localhost'
PORT = 12364

data_file_path = "."

# Declare a global variable to indicate whether the server should continue running
server_is_running = True

def handle_client(conn, addr):
    global server_is_running
    print(f"Accepted connection from {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is ready to accept connections.")
    
    while server_is_running:  # Check the flag before accepting new connections
        # Accept incoming connections
        conn, addr = s.accept()
        
        # Handle client communication in a dedicated thread
        client_thread = Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
    
    s.close()
    sys.exit(0)



