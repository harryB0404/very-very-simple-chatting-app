import socket
import threading
import time
import sys

HOST = 'Put Server IP after run server.py'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def msg_send(client):
    msg = input('__SEND>>  ')
    if msg == "endchat":
        print("YOU ended the chat!")
        data = msg.encode('utf-8')
        client.send(data)
        sys.exit(0)
    else:
        data = msg.encode('utf-8')
        client.send(data)


def print_get(msg):
    print(f"SERVER:  {msg}")
    print("__SEND>>  ", end="", flush=True)


def msg_get(client):
    while True:
        data = client.recv(1024)
        msg = data.decode('utf-8')
        print("\n")
        if msg == "endchat":
            print("SERVER ended the chat!")
            break
        else:
            print_get(msg)


def main():
    try:
        client.connect((HOST, PORT))
        print(f'Successfully connected to SERVER!!!')
        print("")
        print("Press any key and wait... ")
        while True:
            msg_send(client)
            threading.Thread(target=msg_get, args=(client,), daemon=True).start()
    except Exception as e:
        print("ERROR", e)


main()
