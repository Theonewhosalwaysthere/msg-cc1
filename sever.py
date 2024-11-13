import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345       # The port to listen on

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections (with a max backlog of 5)
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}...")

# Handle incoming connections
while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive the message from the client (up to 1024 bytes)
    data = client_socket.recv(1024)

    if data:
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        
        # Send a response back to the client
        response = "Message received!"
        client_socket.sendall(response.encode('utf-8'))
    else:
        print("No data received.")

    # Close the connection with the client
    client_socket.close()
