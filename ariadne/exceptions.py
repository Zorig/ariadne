from .constants import HTTP_STATUS_400_BAD_REQUEST, HTTP_STATUS_405_METHOD_NOT_ALLOWED


class HttpError(Exception):
    status = ""

    def __init__(self, message=None):
        super().__init__()
        self.message = message


class HttpBadRequestError(HttpError):
    status = HTTP_STATUS_400_BAD_REQUEST


class HttpMethodNotAllowedError(HttpError):
    status = HTTP_STATUS_405_METHOD_NOT_ALLOWED


class GraphQLFileSyntaxError(Exception):
    def __init__(self, schema_file, message):
        super().__init__()
        self.message = self.format_message(schema_file, message)

    def format_message(self, schema_file, message):
        return f"Could not load {schema_file}:\n{message}"

    def __str__(self):
        return self.message
