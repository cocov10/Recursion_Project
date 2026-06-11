import socket
import sys
import json

server_address = './tmp/rpc_socket_file'

payload = {
    "method": "subtract",
    "params": [42, 23],
    "param_types": ["int", "int"],
    "id": 1
}

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    try:
        sock.connect(server_address)
    except socket.error as err:
        print(f"サーバーが起動していません。")
        sys.exit(1)

    try:
        # データは少ない想定
        json_data = json.dumps(payload).encode('utf-8')
        sock.sendall(json_data)

        response = sock.recv(1024)

        result = json.loads(response.decode('utf=8'))
        print("サーバーからの返信:")
        print(result)

    except FileNotFoundError:
        print(f"サーバーが起動していません。")



