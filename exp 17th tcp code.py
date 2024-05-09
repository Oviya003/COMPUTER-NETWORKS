import socket

# Define the host and port to listen on
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    # Start listening for incoming connections
    server_socket.listen()
    
    print(f"Server is listening on {HOST}:{PORT}")
    
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        with client_socket:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break
                
                # Echo back the received data
                client_socket.sendall(data)









import socket

# Define the server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    
    # Receive data from the server
    received_data = client_socket.recv(1024)
    print("Received:", received_data.decode())

