
import socket
from datetime import datetime

# Server configuration
HOST = "127.0.0.1"
PORT = 5000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Allow the server to reuse its address after restarting
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Assign the IP address and port
    server_socket.bind((HOST, PORT))

    # Start listening for connections
    server_socket.listen(1)

    print("CYB 333 Server started!")
    print(f"Listening for connections on {HOST}:{PORT}")

    # Wait for a client to connect
    connection, address = server_socket.accept()

    print(f"Client connected from {address}")

    # Record the date and time of the connection
    connection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Connection timestamp: {connection_time}")

    # Automatically close the client connection when finished
    with connection:
        # Receive a message from the client
        message = connection.recv(1024).decode("utf-8")

        if not message:
            print("Client disconnected without sending a message.")
        else:
            print(f"Message received from client: {message}")

            # Create a response
            response = "Hello Client! Your message was received successfully."

            # Send the response to the client
            connection.sendall(response.encode("utf-8"))

            print(f"Response sent to client: {response}")

            # Signal that the server has finished sending data
            connection.shutdown(socket.SHUT_WR)

            print("Server finished sending data.")


except ConnectionResetError:
    # Handle a client disconnecting unexpectedly
    print("Connection error: The client disconnected unexpectedly.")

except OSError as error:
    # Handle other socket-related errors
    print(f"Server error: {error}")

except KeyboardInterrupt:
    # Handle manually stopping the server
    print("\nServer interrupted by user.")

finally:
    # Always close the server socket
    server_socket.close()
    print("Server shut down successfully.")
