import socket

# Server connection information
HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Limit how long the client waits for network operations
client_socket.settimeout(5)


try:
    # Attempt to connect to the server
    client_socket.connect((HOST, PORT))

    print("Successfully connected to the server!")

    # Create a message to send
    message = "Hello Server! This is my CYB 333 client."

    # Send the message to the server
    client_socket.sendall(message.encode("utf-8"))

    print(f"Message sent to server: {message}")

    # Receive the server's response
    response = client_socket.recv(1024).decode("utf-8")

    print(f"Response received from server: {response}")

except ConnectionRefusedError:
    # Handle the error when the server is not running
    print("Connection failed: The server is not running.")
    print("Please start server.py and try again.")

except socket.timeout:
    # Handle a connection timeout
    print("Connection failed: The server took too long to respond.")

except OSError as error:
    # Handle other network-related errors
    print(f"A network error occurred: {error}")

finally:
    # Always close the socket
    client_socket.close()
    print("Client socket closed.")
