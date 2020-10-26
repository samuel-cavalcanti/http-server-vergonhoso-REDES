import unittest

from response import Response
from routes import Routes


class MockRequest:
    METHOD_GET = 0
    method: int
    path: str
    version_of_protocol: str
    headers: str


class TestResponse(unittest.TestCase):
    __index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Este é o meu servidor!</title>
</head>

<body>

<h1>Olá mundo!</h1>
O meu servidor funciona!

</body>
</html>'''
    __bad_request_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bad Request </title>
</head>
<body>
    <h1>D: não usem telnet.</h1>
</body>
</html>'''

    __not_found_html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Not Found</title>
    </head>
    <body>
        <h1>Not found 404</h1>
    </body>
</html>'''

    def __bad_request_html_expected(self) -> bytes:
        return f'HTTP/1.1 400 Bad Request\r\n\r\n{self.__bad_request_html}\r\n'.encode()

    def __not_found_response_expected(self) -> bytes:
        return f'HTTP/1.1 404 Not Found\r\n\r\n{self.__not_found_html}\r\n'.encode()

    def __get_index_response_expected(self) -> bytes:
        return f'HTTP/1.1 200 OK\r\n\r\n{self.__index_html}\r\n'.encode()

    @staticmethod
    def __create_get_index_request():
        request = MockRequest()
        request.method = request.METHOD_GET
        request.path = Routes.index
        request.version_of_protocol = 'HTTP/1.1'
        request.headers = ''
        return request

    @staticmethod
    def __create_bad_request():
        request = MockRequest()
        request.method = request.METHOD_GET
        request.path = Routes.bad_request
        request.version_of_protocol = 'HTTP/1.1'
        request.headers = ''
        return request

    @staticmethod
    def __create_not_found_request():
        request = MockRequest()
        request.method = request.METHOD_GET
        request.path = Routes.not_found
        request.version_of_protocol = 'HTTP/1.1'
        request.headers = ''
        return request

    def test_get_index_request(self):
        status_code = 200
        request = self.__create_get_index_request()
        response = Response(self.__index_html, status_code, request)
        self.assertTrue(response.encode() == self.__get_index_response_expected())

    def test_bad_request_response(self):
        status_code = 400
        request = self.__create_bad_request()
        response = Response(self.__bad_request_html, status_code, request)
        self.assertTrue(response.encode() == self.__bad_request_html_expected())

    def test_not_found_response(self):
        status_code = 404
        request = self.__create_not_found_request()
        response = Response(self.__not_found_html, status_code, request)
        self.assertTrue(response.encode() == self.__not_found_response_expected())


if __name__ == '__main__':
    unittest.main()
