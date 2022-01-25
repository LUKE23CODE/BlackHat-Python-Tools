import socket

target_host = 'localhost'
target_port = 9998

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

print(response)
