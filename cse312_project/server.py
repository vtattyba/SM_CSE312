import socket
import Utils
import os


def main():
    run_server()


def encode_and_send(response, conn):
    try:
        response = response.encode('utf-8', 'ignore')
    except AttributeError:
        a = 'ignore it'
    conn.sendall(response)


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    hp = Utils.HTTPHelper()

    host = ''
    port = int(input('Enter the port you want to use: '))
    server.bind((host, port))
    server.listen()
    while True:
        conn, address = server.accept()
        request = conn.recv(5000)
        request = request.decode()
        hp.parse_request(request)

        if int(hp.get_request().get('Content-Length', 0)) != 0:
            hp.buffer(conn)
            hp.content_parser()
        if request is None or request == '':
            continue

        path = hp.get_request()['Path']
        print(hp.get_request(), '\n', hp.get_content(), '\n###################')

        if path == '/':
            response = hp.serve_content('Index.html', True)
            conn.sendall(response.encode())
        elif path[1:] in os.listdir('Front_End') or (path[1:7] == 'Public'):
            response = hp.serve_content(path[1:], False)
            encode_and_send(response, conn)
        elif path == '/crash':
            break
        else:
            response = hp.serve_content('404_file.html', False)
            conn.send(response.encode())

        print(hp.get_response(), '\n###################')


if __name__ == '__main__':
    main()
