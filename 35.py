import socket
from view35 import index, blog

URLS = {
    '/': index,
    '/blog': blog
}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method, url):
    if method != 'GET':
        return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Method Not Found!\n\n', 404
    return 'HTTP/1.1 200 OK!\n\n', 200  # \n\n


def generete_content(code, url):
    if code == 404:
        return '<h1>404</h1><h3>Not Found</h3>'
    elif code == 405:
        return '<h1>404</h1><h3>Not Allowed</h3>'
    return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generete_content(code, url)
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()  # 127.0.0.1:5000
    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
        response = generate_response(request.decode())
        client_socket.sendall(response)
        client_socket.close()


if __name__ == "__main__":
    run()


