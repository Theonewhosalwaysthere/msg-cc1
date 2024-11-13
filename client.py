import socket

# Server's IP address and port
server_ip = '192.168.1.100'
server_port = 12345  # Replace with the server's actual port

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((server_ip, server_port))

# Send the message
message = 'Hello, Server!'

try:
    # Send data to the server
    sock.sendall(message.encode('utf-8'))
    print(f'Message sent: {message}')
    
    # Receive the response (if any)
    response = sock.recv(1024)
    print('Response from server:', response.decode('utf-8'))

finally:
    # Close the socket connection
    sock.close()
