import socket
import threading
import sys
import time

HOST = socket.gethostbyname(socket.gethostname()) #your ipv4
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(HOST)

def write_txt(msg):
    with open("log.txt", "w") as f:
        f.write(msg + "\n")

def print_get(msg):
    print(f"CLIENT:  {msg}")
    print("__SEND>>  ", end="", flush=True)
def msg_get(conn):
    while True:
        try:
            data = conn.recv(1024)
            msg = data.decode('utf-8')
            print("\n")
            write_txt(msg)

            if msg == "endchat":
                print("CLIENT ended the chat!")
                print("__SEND>>  ", end="", flush=True)
                break
            else:
                print_get(msg)

        except:
            print("\nLost connection with server!")
            sys.exit(0)



def msg_send(conn):
    msg = input('__SEND>>  ')
    time.sleep(0.1)
    if msg == "endchat":
        print("YOU ended the chat!")
        data = msg.encode('utf-8')
        conn.send(data)
        sys.exit(0)
    else:
        write_txt(msg)
        data = msg.encode('utf-8')
        conn.send(data)



def start():
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"SERVER IS RUNNING..... WAITING FOR CONNECTION... ")

def show_menu():
    print("")
    print("---------------------")
    print("Option 1: Start server")
    print("Option 2: Close")

def choose(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice)>max:
        print(f"'{choice}' is not an Option! Please Re-enter!")
        choice = input(prompt)
    else:
        return int(choice)


def main1():

        try:
            start()
            conn, addr = server.accept()
            print(f"New connection from {addr}")
            print("")
            print("Press any key and wait... ")
            while True:
                msg_send(conn)
                #msg_get(conn)
                threading.Thread(target=msg_get, args=(conn,), daemon=True).start()
        except Exception as e:
            print("ERROR", e)


def main():
    show_menu()
    choice = choose("Enter an option (1-2):  ", 0, 5)

    if choice == 1:
        main1()
    elif choice == 2:
        sys.exit(0)
    elif choice == 3:
        menu_3
    elif choice == 4:
        menu_4
    elif choice == 5:
        menu_5
    else:
        main()


main()