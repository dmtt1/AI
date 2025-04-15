import socket
import bisect

# Define server address and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print("[*] UDP Server listening on", SERVER_HOST, SERVER_PORT)

# Read and sort pincode data from file
def load_and_sort_pincode_file(filename):
    with open(filename, 'r') as f:
        pin_codes = f.read().splitlines()  # Read each line (pincode)
        pin_codes = [int(pincode) for pincode in pin_codes]
        pin_codes.sort()  # Sorting pin codes in ascending order
    return pin_codes

# Binary search function (O(log n) complexity)
def search_pincode(pincode, pin_codes):
    index = bisect.bisect_left(pin_codes, pincode)
    if index < len(pin_codes) and pin_codes[index] == pincode:
        return True  # Pincode found
    return False  # Pincode not found

# Load and sort the pin codes once
pin_codes = load_and_sort_pincode_file('pincode.txt')

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    pincode = int(data.decode())  # Convert received data to an integer

    print(f"[*] Received pincode: {pincode} from {client_address}")

    # Search for the pincode in the sorted list
    found = search_pincode(pincode, pin_codes)

    # Send result to the client
    if found:
        response = f"Pincode {pincode} found."
    else:
        response = f"Pincode {pincode} not found."
    
    # Send the response back to the client
    server_socket.sendto(response.encode(), client_address)
    
   
