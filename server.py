import socket
import threading
from agents import EnvironmentalAgent, TechnologyAgent
host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
env_agent = EnvironmentalAgent()
tech_agent = TechnologyAgent()

print("Server is running...")

def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

def handle_client(client):

    while True:

        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            print("Received:", message)

            env_response = env_agent.analyze(message)
            tech_response = tech_agent.analyze(message)

            # broadcast original message
            broadcast(message.encode("utf-8"), None)

            # send AI responses
            if env_response:
                broadcast(env_response.encode("utf-8"), None)

            if tech_response:
                broadcast(tech_response.encode("utf-8"), None)

        except:
            clients.remove(client)
            client.close()
            break

while True:
    client, addr = server.accept()
    print(f"Connected with {addr}")
    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
