import socket
import os
import sys
import json

# sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './tmp/rpc_socket_file'

if os.path.exists(server_address):
    os.remove(server_address)

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    sock.bind(server_address)
    sock.listen(1)
    print(f"サーバー起動中..({server_address})")

    # クライアントからの接続を待ち続ける
    while True:
        connection, client_address = sock.accept()
        with connection:
            print(f"クライアントの接続: {client_address}")
            # サーバーが新しいデータを待ち続ける　データが多い場合
            # while True:
            # 今回はデータは少ない想定
            data = connection.recv(1024)                
            if not data:
                print("データがありません。", client_address)
                break

            request_json = json.loads(data.decode('utf-8'))
            print(f"受信したJSON: {request_json}")

            # 返信
            response_data = {
                "results": "19",
                "result_type": "int",
                "id": 1
            }

            response_json = json.dumps(response_data).encode('utf-8')
            connection.sendall(response_json)
            

            
