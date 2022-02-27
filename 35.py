import socket


URLS = {
    "/": "index page",
    "/blog": "blog page"
}

def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url

def generate_haeaders(method, url):
    if method != "GET":
        return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Method Not Found!\n\n', 404
    return 'HTTP/1.1 200 OK!', 200

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen() # 127.0.0.1:5000 оращается к порту

    while True:
        client_socket, addres = server_socket.accept()
        requests = client_socket.recv(1024)
        print(f'Клиент: {addres}=>\n{requests.decode("utf-8")}\n')


if __name__ == "__main__":
    run()


