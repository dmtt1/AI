import socket

# Define server address and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8888

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send data to server
client_socket.sendall("Hello from client!".encode())

# Receive response from server
data = client_socket.recv(1024)
print("[*] Received from server:", data.decode())

# Close the connection
client_socket.close()

# 1) Use TCP SOCKET
# Create TXT file containing Pincode in random order
# client should send pincode to searched to server
# at server side you should serach the pincode from the file.
#!! Most Important Time cpomplaxity should be O(log n)!!
