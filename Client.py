from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import os
from dotenv import load_dotenv
load_dotenv()


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break


def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("ChatBox")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("")
scrollbar_x = tkinter.Scrollbar(messages_frame, orient=tkinter.HORIZONTAL)
scrollbar_y = tkinter.Scrollbar(messages_frame)

msg_list = tkinter.Listbox(
    messages_frame, 
    height=25, 
    width=90,)

scrollbar_x.config(command=msg_list.xview)
scrollbar_y.config(command=msg_list.yview)

scrollbar_x.pack(side=tkinter.BOTTOM, fill=tkinter.X)
scrollbar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

msg_list.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

# msg_list.pack()
messages_frame.pack()

message_label = tkinter.Label(top, text="Message: ")
message_label.pack(side=tkinter.LEFT)

entry_field = tkinter.Entry(top, textvariable=my_msg, width=60)
entry_field.bind("<Return>", send)
entry_field.pack(side=tkinter.LEFT)

send_button = tkinter.Button(top, text="Send", command=send, width=20)
send_button.pack(side=tkinter.RIGHT,fill=tkinter.X)

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
BUFSIZ = int(os.getenv('BUFSIZ'))
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

print("Connection with Server established !!!")

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()