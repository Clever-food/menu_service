import peewee
from typing import Type

from pydantic import ValidationError

from .base_http_exception import BaseHTTPException


class UnknownError(BaseHTTPException):
    _message = f""
    _error_code = 1
    _status_code = 500

    def __init__(
            self,
            exception: Exception,
    ):
        super().__init__()
        self._message = f"Unhandled error {exception}"
        

class ValidationHTTPError(BaseHTTPException):
    _message = f""
    _error_code = 1
    _status_code = 422

    def __init__(
            self,
            exception: ValidationError
    ):
        super().__init__()
        self._message = []
        for error_info in exception.errors():
            self._message.append(
                {
                    "value": str(error_info['input']),
                    "field": str(error_info['loc'][-1]),
                    "message": error_info['msg'],
                }
            )


class EntityDoesNotExistError(BaseHTTPException):
    _message = f""
    _error_code = 2
    _status_code = 400

    def __init__(
            self,
            model_class: Type[peewee.Model],
    ):
        super().__init__()
        self._message = f"Entity does not exist in table {model_class.__name__}"


class EntityAlreadyExistsError(BaseHTTPException):
    _message = f""
    _error_code = 3
    _status_code = 400

    def __init__(
            self,
            model_class: Type[peewee.Model],
    ):
        super().__init__()
        self._message = f"Entity is already exist in table {model_class.__name__}"

class DuplicateEntityError(BaseHTTPException):
    _message = f""
    _error_code = 4
    _status_code = 400

    def __init__(
            self,
            model_class: Type[peewee.Model],
            fieldname: str
    ):
        super().__init__()
        self._message = f"Entity with that value of {fieldname} is already exist in table {model_class.__name__}"


class CameraNotFoundError(BaseHTTPException):
    _message = f""
    _error_code = 5
    _status_code = 400

    def __init__(
            self,
    ):
        super().__init__()
        self._message = f"Camera not found error"


class NoSpaceError(BaseHTTPException):
    _message = f""
    _error_code = 6
    _status_code = 400

    def __init__(
            self,
    ):
        super().__init__()
        self._message = f"No space left on device"


class ForeignKeyError(BaseHTTPException):
    _message = f""
    _error_code = 7
    _status_code = 400

    def __init__(
            self,
            model_class: Type[peewee.Model],
            fieldname: str
    ):
        super().__init__()
        self._message = f"Cannot create entity in table {model_class}, no such '{fieldname}' in parent table"


class FrameFileNotFoundError(BaseHTTPException):
    _message = f""
    _error_code = 8
    _status_code = 400

    def __init__(
            self,
    ):
        super().__init__()
        self._message = f"The frame was not found in the storage"

class EntityNoMinimumLength(BaseHTTPException):
        _message = f""
        _error_code = 3
        _status_code = 400

        def __init__(
                self,
                model_class: Type[peewee.Model],
        ):
                super().__init__()
                self._message = f"Minimum length must be 3 characters"
