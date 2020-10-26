import unittest

from http_server import HttpServer
from routes import Routes


class MockRequest:
    METHOD_GET = 0
    method: int
    path: str
    version_of_protocol: str
    headers: str


class TestHttpServer(unittest.TestCase):
    __server = HttpServer()

    def test_get_index(self):
        html_content, status_code = self.__server.get("/")
        self.__verify_get_index_content(html_content, status_code)

    def __check_not_found(self, path: str):
        html_content, status_code = self.__server.get(path)
        self.assertTrue('Not found' in html_content)
        self.assertTrue(status_code, 404)

    def test_get_not_found(self):
        self.__check_not_found("asdadsadsad")
        self.__check_not_found("not found")
        self.__check_not_found("")

    def __verify_get_index_content(self, html: str, status_code: int):
        self.assertTrue('Este é o meu servidor!' in html)
        self.assertTrue(status_code, 200)
        pass

    @staticmethod
    def __create_request():
        request = MockRequest()
        request.method = request.METHOD_GET
        request.path = Routes.index
        request.version_of_protocol = 'HTTP/1.1'
        request.headers = ''
        return request

    def test_response_to_request(self):
        request = self.__create_request()
        html_content, status_code = self.__server.response_to(request)
        self.__verify_get_index_content(html_content, status_code)


if __name__ == '__main__':
    unittest.main()
