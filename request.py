from routes import Routes


class Request:
    METHOD_GET = 0
    METHOD_POST = 1
    METHOD_DELETE = 3
    METHOD_PUT = 4

    method: int
    path: str
    version_of_protocol: str
    headers: str

    __block_of_bytes: bytes
    __method_decoder = {
        'GET': METHOD_GET,
        'POST': METHOD_POST,
        'DELETE': METHOD_DELETE,
        'PUT': METHOD_PUT
    }

    def __init__(self, block_of_bytes: bytes):
        self.__block_of_bytes = block_of_bytes
        self.__decode()
        pass

    def __decode(self):
        try:
            string = self.__block_of_bytes.decode('utf-8')
            first_line, self.headers = string.split('\n', maxsplit=1)
            self.__decode_first_line(first_line)
        except Exception as e:
            self.__become_bad_request()

    def __decode_first_line(self, first_line: str):
        method, self.path, self.version_of_protocol = first_line.split(' ')
        self.method = self.__method_decoder.get(method, False)
        if not method:
            raise Exception('Method is not implemented')

    def __become_bad_request(self):
        self.method = self.METHOD_GET
        self.path = Routes.bad_request
        self.headers = ''
        self.version_of_protocol = 'HTTP/1.1'
