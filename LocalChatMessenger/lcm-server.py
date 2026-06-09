# lcm-server,py
# /home/root01/python_practice/recursion_project/LocalChatMessenger
# python_practice/recursion_project/LocalChatMessenger

import socket
import os
from faker import Faker

fake = Faker('ja_JP')

# TCP
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './tmp/lcm_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)

            if data:
                data_str = data.decode('utf-8')
                print('Received ' + data_str)
                fake_name = fake.name()
                # fake_address = fake.address()
                # response = f'Hi I am {fake_name}, \nI living {fake_address}' 
                # fake_catch = fake.catch_phrase()
                # response = f"hello I am {fake_name}, {fake_catch}"
                response = fake.text(max_nb_chars=200)
                connection.sendall(response.encode('utf-8'))
            else:
                print('no data from', client_address)
                break

    finally:
        print("Closing current connection")
        connection.close()




