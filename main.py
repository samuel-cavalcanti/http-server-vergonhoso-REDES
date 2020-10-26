# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

import socket

from http_server import HttpServer
from request import Request
from response import Response

HOST = ''
PORT = 8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))

listen_socket.listen(1)

print('Serving HTTP on port %s ...' % PORT)

http_server = HttpServer()

while True:
    client_connection, client_address = listen_socket.accept()

    block_of_bytes = client_connection.recv(1024)

    request = Request(block_of_bytes)
    if request.method == Request.METHOD_GET:
        print(block_of_bytes.decode())

    html_content, status_code = http_server.response_to(request)

    response = Response(html_content, status_code, request)

    client_connection.send(response.encode())

    client_connection.close()

listen_socket.close()
