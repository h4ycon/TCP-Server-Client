import socket

SERVER = 'localhost'
PORT = 12345
BUFFER_SIZE = 1024
transmission_flag = True
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER, PORT))

while transmission_flag:
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

# With these new lines:
username = "your_username"
password = "your_password"
message = f"{username}:{password}"
client_socket.sendall(message.encode())

received_data = client_socket.recv(BUFFER_SIZE)
print(f"Received data: {received_data.decode('utf-8')}")

client_socket.close()