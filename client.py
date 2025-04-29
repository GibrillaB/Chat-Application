import socket
import threading

host = '127.0.0.1'
port = 55555

# Prompt for a username
username = input("Enter your username: ")

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("An error occurred while receiving messages. Disconnecting...")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            if message.lower() == "/quit":
                client_socket.send(f"{username} has left the chat.".encode('utf-8'))
                client_socket.close()
                break
            full_message = f"{username}: {message}"
            client_socket.send(full_message.encode('utf-8'))
        except:
            print("An error occurred while sending. Disconnecting...")
            client_socket.close()
            break

# Create and connect the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except Exception as e:
    print(f"Unable to connect to server: {e}")
    exit()

# Send the username for joining
client.send(f"{username} has joined the chat.".encode('utf-8'))

# Start session
receive_thread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client,), daemon=True)
send_thread.start()

# Keep the main thread alive
receive_thread.join()
send_thread.join()
