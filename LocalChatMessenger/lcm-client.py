import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './tmp/lcm_socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        user_input = input("最近どうですか？('exit'で終了): ")
        
        if user_input.lower() == 'exit':
            print('終了します。')
            break
        
        message = user_input.encode('utf-8')
        sock.sendall(message)

        sock.settimeout(2)

        try:
            while True:
                data = sock.recv(1024)

                if data:
                    print('Server response:' + data.decode('utf-8'))
                else:
                    break

        except(TimeoutError):
            print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()

