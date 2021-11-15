from abc import ABCMeta
from collections import namedtuple


class ConstMeta(ABCMeta):
    def __setattr__(self, name, value):
        pass


class Const(metaclass=ConstMeta):
    """Helper class """
    __slots__ = ()


class RequestConst(Const):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATH = 'path'
    URL = 'url'
    QUERY = 'query'
    METHOD = 'method'
    TIMEOUT = 'timeout'
    API_PATH = 'api_path'
    PROTOCOL = 'protocol'
    URL_PARAMETERS = 'url_parameters'
    QUERY_PARAMETERS = 'query_parameters'
    DEFAULT_PARAMETERS = 'default_parameters'
    PARAMS_URL_ENCODED = 'params_url_encoded'


class StatusConst(Const):
    SUCCESS = 'success'
    ERROR = 'error'
    SUBMITTED = 'submitted'


class ResponseConst(Const):
    STATUS_KEY = 'status'
    REASON_KEY = 'reason'


class DefaultResponseSuccess(Const):
    ResponseConst.STATUS_KEY = StatusConst.SUCCESS


class DefaultResponse(Const):
    INVALID_RESPONSE = namedtuple(
        'InvalidResponse',
        [ResponseConst.STATUS_KEY, ResponseConst.REASON_KEY]
    )(StatusConst.ERROR, 'Invalid response from server')

    SUCCESS = namedtuple(
        'Success',
        [ResponseConst.STATUS_KEY]
    )(StatusConst.SUCCESS)


class ErrorConst(Const):
    STATUS_KEY = 'status'
    DESCRIPTION_KEY = 'description'
    DEFAULT_DESCRIPTION = 'Unknown error'
    DESCRIPTION_KEYS = ['reason', 'message']


class FormatterConst(Const):
    JSON = 'json'
    FORMATTED = 'formatted'


class TestConst(Const):
    FAKE_RESPONSE_PATH = 'fake_response_path'


class ResponseCode(Const):
    OK_200 = 200
    ACCEPTED_202 = 202
    NO_CONTENT_204 = 204
    NOT_FOUND_404 = 404
    BAD_REQUEST_400 = 400

    ALLOW_EMPTY_RESPONSE = [
        OK_200,
        ACCEPTED_202,
        NO_CONTENT_204
    ]


class BoolConst(Const):
    TRUE = '1'
    FALSE = '0'


class MiscConst(Const):
    FORMAT = 'format'
    PRINT_PARAMS = 'print_params'


class ClientConst(Const):
    META = 'meta'
    MODEL = 'model'
    MODELS = 'models'
    HEADER = 'header'
    FORMATTER = 'formatter'
    DESCRIPTION = 'description'
    PAYLOAD_FORMAT = 'payload_format'
    FORCE_SINGLE_MODEL_RESPONSE = 'force_single_model_response'


class DebugConst(Const):
    PARAMETERS = 'parameters'
    RESPONSE = 'response'
    STATUS_CODE = 'status code'
    FINAL_URL = 'final url'
    HEADERS = 'headers'
    METHOD = 'method'
    QUERY_PARAMETERS = 'query parameters'
    CURL = 'curl'

