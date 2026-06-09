import socket
import os
import random
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
                fake_company = fake.company()
                fake_sentence = fake.sentence()
                templates = [
                    f"{fake_name}さんも同じごと言ってましたよ。「{fake_sentence}」って。",
                    f"そうなんですね。{fake_company} の人たちもよくそんな話をしています。",
                    f"なるほど、「{data_str}」なんですね。よく{fake_sentence}といいますよね。"
                ]
                response = templates[random.randint(0,2)]
                connection.sendall(response.encode('utf-8'))
            else:
                print('no data from', client_address)
                break

    finally:
        print("Closing current connection")
        connection.close()




