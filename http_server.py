from request import Request
from routes import Routes


class HttpServer:
    __supported_paths = {Routes.index: 'views/index.html',
                         Routes.not_found: 'views/not_found.html',
                         Routes.bad_request: 'views/bad_request.html'
                         }

    def get(self, path: str) -> (str, int):
        file_name = self.__supported_paths.get(path, False)

        if not file_name:
            return self.__not_found_page(), 404

        return self.__load_html_file(file_name), 200

    def response_to(self, request: Request):
        if request.METHOD_GET == request.method:
            return self.get(request.path)
        else:
            raise Exception('Only implemented GET method')

    def __not_found_page(self) -> str:
        return self.__load_html_file(self.__supported_paths[Routes.not_found])

    @staticmethod
    def __load_html_file(file_name: str) -> str:
        with open(file_name) as file:
            return file.read()