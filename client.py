import socket
import threading

host = '127.0.0.1'
port = 55555

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error has occurred. Unable to receive message. Closing...")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except:
            print("An error occurred while sending. Closing...")
            client_socket.close()
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client,))
send_thread.start()