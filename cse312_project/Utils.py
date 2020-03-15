import os


class HTTPHelper:

    def __init__(self):
        self.request = {}
        self.response = ''
        self.seen = False
        self.b_arr = b''
        self.client_to_content = {}
        self.content = []

    def get_request(self):
        return self.request

    def get_last_page(self):
        return self.request.get('Referer', 'NA').replace(self.request.get('Origin', 'NA') + '/', '')

    def get_response(self):
        return self.response

    def get_content(self):
        return self.content

    def content_parser(self):
        self.content = []
        boundary = self.get_request()['boundary'].encode()
        content_block = []

        lst = self.b_arr.split(boundary)
        for content in lst:
            content = content.replace(b'--', b'')
            if content == b'' or content == b'\r\n':
                continue
            print(content)
            value_i = content.index(b'\r\n\r\n') + 4
            value = content[value_i:]
            value = value.replace(b'\r\n', b'')
            print('value:', value)
            content = content.replace(b'\r\n\r\n' + value + b'\r\n', b'')
            content = content.replace(b'\r\n', b'')
            for h in content.split(b'; '):
                content_block.append(h)
            content_block.append(value)
            self.content.append(content_block)
            content_block = []
        self.b_arr = b''
        print(self.content, '\n\n')

    def parse_request(self, request):
        self.request = {}
        if request is None or request == '':
            return
        request_lst = request.split('\r\n')
        first_line = request_lst.pop(0)
        line_lst = first_line.split(' ')
        request_lst = ['Request_type: ' + line_lst[0], 'Path: ' + line_lst[1], 'Version: ' + line_lst[2]] + request_lst[
                                                                                                            0:-2]
        boundary = None
        idx = -1
        for elem in request_lst:
            if elem == '':
                idx = request_lst.index(elem)
                break
            else:
                lst = elem.split(': ')
                if lst[0] == 'Content-Type':
                    lst2 = lst[1].split(';')
                    lst3 = lst2[1].split('=')
                    boundary = lst3[1]
                    self.request['boundary'] = boundary
                self.request[lst[0]] = lst[1]
        if boundary is not None:
            self.b_arr += request[request.index('\r\n\r\n') + 4:].encode()

    def create_response(self, response_code, response_headers, content, index_bool):
        """
            response_code is a sting with the number and message of response code. Do not end with ' ' or '\r\n'
            response_headers is a list of the headers you want in the response. Do not end any header with a ' ' ir '\r\n'
            content is the content you want sent to the sever (should be the same size as the Content-Length: VAL's VAL)
            """
        response = 'HTTP/1.1 ' + response_code + '\r\n'
        for header in response_headers:
            response = response + header + '\r\n'
        self.response = response + '\r\n'
        response = response + '\r\n' + content + '\r\n'
        return response

    def create_responseIMG(self, response_code, response_headers, content):
        response = 'HTTP/1.1 ' + response_code + '\r\n'
        for header in response_headers:
            response = response + header + '\r\n'
        self.response = response + '\r\n'
        response = response.encode('utf-8') + '\r\n'.encode('utf-8') + content + '\r\n'.encode('utf-8')
        return response

    def serve_content(self, file_n, index_bool):
        file_n = 'Front_End/' + file_n
        file_type = file_n[file_n.index('.') + 1:]
        if file_type[-1] != 'g':
            file_o = open(file_n, 'r')
            print(file_n)
            print(file_o)
            read = file_o.read()
            return self.create_response('201 OK', ['Content-Type: text/' + file_type,
                                                   'Content-Length: ' + str(len(bytes(read, 'utf-8')))], read,
                                        index_bool)
        else:
            if file_n not in os.listdir('Front_End'):
                file_n = file_n.replace('Front_End/', '')
            img = open(file_n, "rb")
            read = img.read()
            return self.create_responseIMG('201 OK',
                                           ['Content-Type: image/' + file_type, 'Content-Length: ' + str(len(read))],
                                           read)


    def buffer(self, conn):
        length = len(self.b_arr)
        while length < int(self.get_request()['Content-Length']):
            c = conn.recv(5000)
            self.b_arr += c
            length = len(self.b_arr)
