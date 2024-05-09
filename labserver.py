import socket
import time
import threading

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 80)

server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print(f'Server listening on {server_address}...')

# Dictionary to store client IP addresses and their request timestamps
client_registry = {}

# List to store banned IP addresses
banned_ips = []

def handle_client(client_socket, client_address):
    print(f'Connected by {client_address}')

    # Get the client's IP address
    client_ip = client_address[0]

    # Check if the client is banned
    if client_ip in banned_ips:
        print(f'Banned client {client_ip} tried to connect!')
        client_socket.close()
        return

    # Add the client's request timestamp to the registry
    if client_ip not in client_registry:
        client_registry[client_ip] = [time.time()]
    else:
        client_registry[client_ip].append(time.time())

    # Close the client socket
    client_socket.close()

def start_server():
    while True:
        # Wait for a client to connect
        client_socket, client_address = server_socket.accept()

        # Handle the client in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def command_loop():
    while True:
        # Get the administrator's command
        command_from_admin = input("labserver> ")

        # Parse the command
        command_parts = command_from_admin.split()
        if len(command_parts) < 2:
            print(f'Invalid command: {command_from_admin}')
            continue

        command_name = command_parts[0].lower()
        command_args = command_parts[1:]

        # Execute the command
        if command_name == 'blockip':
            if len(command_args)!= 2:
                print(f'Invalid arguments for blockip command: {command_from_admin}')
                continue

            block_ip = command_args[0]

            # Resolve the IP address using DNS
            try:
                block_ip = socket.gethostbyname(block_ip)
            except socket.gaierror:
                print(f'Invalid IP address or domain name: {block_ip}')
                continue

            block_time = command_args[1]

            if block_time == 'q':
                print(f'Banning {block_ip} permanently!')
                banned_ips.append(block_ip)
            else:
                try:
                    block_time = int(block_time)
                except ValueError:
                    print(f'Invalid block time: {block_time}')
                    continue

                print(f'Banning {block_ip} for {block_time} seconds!')
                threading.Timer(block_time, lambda: banned_ips.remove(block_ip)).start()

        elif command_name == 'echo':
            if len(command_args) < 1:
                print(f'Invalid arguments for echo command: {command_from_admin}')
                continue

            message = ' '.join(command_args)
            print(f'Sending message: {message}')

        elif command_name == 'blockevery':
            print(f'Banning all clients!')
            for ip in client_registry:
                if ip not in banned_ips:
                    banned_ips.append(ip)
                    print(f'Banned {ip} permanently!')

        else:
            print(f'Unknown command: {command_from_admin}')

if __name__ == '__main__':
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Start the command loop
    command_loop()