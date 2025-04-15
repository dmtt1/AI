import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # Localhost for testing
SERVER_PORT = 5555

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Pincode to search
pincode = 12345  # Replace with the pincode you'd like to search for

# Send pincode to server
client_socket.sendto(str(pincode).encode(), (SERVER_HOST, SERVER_PORT))

# Receive the response from the server
data, server_address = client_socket.recvfrom(1024)
print("[*] Received from server:", data.decode())

# Close the client socket
client_socket.close()
