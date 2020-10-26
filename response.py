from request import Request


class Response:
    __content: str
    __message_of_status_code = {
        200: 'OK',
        404: 'Not Found',
        400: 'Bad Request'
    }
    __end_line = '\r\n'

    def __init__(self, html_content: str, status_code: int, request: Request):
        self.__make_fist_line_of_response_message(request, status_code)
        self.__add_html_content(html_content)
        pass

    def __make_fist_line_of_response_message(self, request: Request, status_code: int):
        status_code_message = self.__message_of_status_code.get(status_code, False)
        if not status_code_message:
            raise Exception(f'status code not implemented: {status_code}')

        self.__content = f'{request.version_of_protocol} {status_code} {self.__message_of_status_code[status_code]}' \
                         f'{self.__end_line * 2}'

    def __add_html_content(self, html: str):
        self.__content += f'{html}{self.__end_line}'

    def encode(self):
        return self.__content.encode()
