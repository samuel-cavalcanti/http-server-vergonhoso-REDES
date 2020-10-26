import unittest

from request import Request
from routes import Routes


class RequestTest(unittest.TestCase):

    def test_get_root_path(self):
        request = self.__decode_request('GET / HTTP/1.1\n')
        self.assertTrue(Request.METHOD_GET == request.method)
        self.assertTrue(request.version_of_protocol == "HTTP/1.1")
        self.assertTrue(request.path == "/")

    def test_post_root_path(self):
        request = self.__decode_request('POST / HTTP/1.1\n')
        self.assertTrue(Request.METHOD_POST == request.method)

    def test_bad_request(self):
        message_without_end_line = 'GET / HTTP/1.1'
        request = self.__decode_request(message_without_end_line)

        self.assertTrue(request.path == Routes.bad_request)
        self.assertTrue(request.version_of_protocol == 'HTTP/1.1')
        self.assertTrue(request.METHOD_GET == request.method)

    @staticmethod
    def __decode_request(message: str) -> Request:
        return Request(message.encode())


if __name__ == '__main__':
    unittest.main()
