import requests
from abc import ABCMeta
from urllib.parse import urlencode

from gupshup_python_api_client import constants
from gupshup_python_api_client.debug import Debug
from gupshup_python_api_client.response import Response
from gupshup_python_api_client.formatter import FormatterFactory
from gupshup_python_api_client.exceptions import RequestApiException


class Api(metaclass=ABCMeta):
    """Abstract API class."""


def bind_request(**request_data):
    """Binds request class to client property, dynamically."""

    class Request(Api):
        """Request class. Does the actual API request."""

        model = request_data.get(constants.ClientConst.MODEL)
        api_path = request_data.get(constants.RequestConst.API_PATH)
        payload_format = request_data.get(constants.ClientConst.PAYLOAD_FORMAT)
        formatter = request_data.get(constants.ClientConst.FORMATTER)
        header = request_data.get(constants.ClientConst.HEADER) or {}
        method = request_data.get(
            constants.RequestConst.METHOD, constants.RequestConst.GET
        )
        query_parameters = request_data.get(
            constants.RequestConst.QUERY_PARAMETERS
        )
        url_parameters = request_data.get(
            constants.RequestConst.URL_PARAMETERS
        )
        file_parameters = request_data.get(
            constants.RequestConst.FILE_PARAMETERS
        )
        fake_response_path = request_data.get(
            constants.TestConst.FAKE_RESPONSE_PATH
        )
        default_parameters = request_data.get(
            constants.RequestConst.DEFAULT_PARAMETERS, {}
        )
        # immediately determine type of response
        single_model_response = request_data.get(
            constants.ClientConst.FORCE_SINGLE_MODEL_RESPONSE, False
        ) or method in [
            constants.RequestConst.POST,
            constants.RequestConst.PUT,
            constants.RequestConst.DELETE
        ]

        def __init__(self, client, debug: 'Debug',
                     *path_params, **query_params):
            client.request = self

            self.url = None
            self.debug = debug
            self.client = client
            self.parameters = {
                constants.RequestConst.QUERY: {},
                constants.RequestConst.URL: {},
                constants.RequestConst.FILE: {},
                constants.RequestConst.PATH: []
            }

            self._timeout = 15

            self._set_parameters(*path_params, **query_params)

        def _set_parameters(self, *path_params, **query_params):
            """
            Prepares the list of query parameters
            :path_params: list of path parameters
            :query_params: dict of query parameters
            :return: None
            """

            # take timeout
            try:
                self._timeout = int(query_params.get(
                    constants.RequestConst.TIMEOUT, self._timeout
                ))
            except ValueError:
                pass
            try:
                del query_params[constants.RequestConst.TIMEOUT]
            except KeyError:
                pass

            # set default API call params
            for key, value in self.default_parameters.items():
                self.parameters[constants.RequestConst.QUERY][key] = value

            _query_params = self.query_parameters.get_params()

            if self.url_parameters:
                _url_params = self.url_parameters.get_params()
            else:
                _url_params = {}

            if self.file_parameters:
                _file_params = self.file_parameters.get_params()
            else:
                _file_params = {}

            # set API call params defined during the "call" invocation
            for key, value in query_params.items():
                if value is None:
                    continue

                if key in _url_params.values():
                    self.parameters[constants.RequestConst.URL][key] = value

                if key in _file_params.values():
                    self.parameters[constants.RequestConst.FILE][key] = value

                if key in _query_params.values():
                    self.parameters[constants.RequestConst.QUERY][key] = value

                elif key in _query_params.keys():
                    self.parameters[
                        constants.RequestConst.QUERY
                    ][_query_params[key]] = value

            if self.method == constants.RequestConst.GET:
                # transform all True and False param to 1 and 0
                for key, value in self.parameters[
                    constants.RequestConst.QUERY
                ].items():
                    if value is True:
                        self.parameters[constants.RequestConst.QUERY][key] = \
                            constants.BoolConst.TRUE
                    if value is False:
                        self.parameters[constants.RequestConst.QUERY][key] = \
                            constants.BoolConst.FALSE

            # set optional url path params
            for value in path_params:
                self.parameters[constants.RequestConst.PATH].append(value)

        def _prepare_url(self):
            """
            Prepares url and query parameters for the request
            :return: URL
            """

            base_url = '{}://{}{}'.format(
                self.client.protocol, self.client.base_url, self.api_path
            )
            url_parts = '/'.join(
                [part for part in self.parameters[constants.RequestConst.PATH]]
            )

            if url_parts:
                final_url = '{}/{}'.format(base_url, url_parts)
            else:
                final_url = base_url

            if self.method == constants.RequestConst.GET:
                params = self.parameters[constants.RequestConst.QUERY]
            else:
                params = self.parameters[constants.RequestConst.URL]

            used_params = []
            for param, value in params.items():
                if f'<{param}>' in final_url:
                    final_url = final_url.replace(f'<{param}>', value)
                    used_params.append(param)

            for param in used_params:
                del params[param]

            if params:
                for param, value in params.items():
                    if isinstance(value, list):
                        params[param] = ','.join(value)
                    elif isinstance(value, dict):
                        params[param] = ','.join([f'{k}:{v}' for k, v in value])

                url_query = '?' + '&'.join([f'{k}={v}' for k, v in params.items()])
                final_url = '{}{}'.format(final_url, url_query)

            self.debug.ok(constants.DebugConst.FINAL_URL, final_url)

            return final_url

        def _headers(self):
            """Construct headers data with authentication part"""

            headers = {
                **self.__class__.header,
                'User-Agent': 'Gupshup Python API Client'
            }
            if self.client.api_key:
                headers = {
                    **headers,
                    'apikey': self.client.api_key
                }
            if self.client.api_token:
                headers = {
                    **headers,
                    'token': self.client.api_token
                }

            self.debug.ok(constants.DebugConst.HEADERS, headers)

            return headers

        def _do_request(self, url: str):
            """
            Makes the request to Sendbee Api servers
            :url: Url for the request
            :return: Tuple with two elements, status code and content
            """

            self.debug.ok(constants.DebugConst.METHOD, self.method)

            if self.client.fake_response_path:
                with open(self.client.fake_response_path, 'r') as f:
                    return constants.ResponseCode.OK_200, f.read()

            elif self.method == constants.RequestConst.GET:
                response = requests.get(
                    url, headers=self._headers(), timeout=self._timeout
                )

                self.debug.ok(
                    constants.DebugConst.QUERY_PARAMETERS,
                    self.parameters[constants.RequestConst.QUERY]
                )
                self.debug.ok(
                    constants.DebugConst.RESPONSE, response
                )
                self.debug.set_curl(
                    constants.DebugConst.CURL,
                    response.request
                )

                return response.status_code, response.text

            elif self.method in [
                constants.RequestConst.POST,
                constants.RequestConst.PUT,
                constants.RequestConst.DELETE
            ]:
                if self.method == constants.RequestConst.POST:
                    send_request = requests.post
                elif self.method == constants.RequestConst.PUT:
                    send_request = requests.put
                elif self.method == constants.RequestConst.DELETE:
                    send_request = requests.delete

                if self.__class__.payload_format == \
                        constants.RequestConst.PARAMS_URL_ENCODED:
                    payload = urlencode(
                        self.parameters[constants.RequestConst.QUERY])
                else:
                    payload = self.parameters[constants.RequestConst.QUERY]

                if self.parameters[constants.RequestConst.FILE]:
                    files = self.parameters[constants.RequestConst.FILE]
                else:
                    files = None

                print(files)
                print(self.parameters)

                response = send_request(
                    url, data=payload, files=files,
                    headers=self._headers(), timeout=self._timeout
                )
                # class response:
                #     text = '{"status":"success","template":{"category":' \
                #            '"AUTO_REPLY","createdOn":1625843483030,"data":' \
                #            '"Hi {{1}}, thank you for contacting Sendbee. ' \
                #            'How can we help you?","elementName":' \
                #            '"haw_can_we_help_you","id":' \
                #            '"e26b39d5-3928-4e5a-b197-277a342ab709",' \
                #            '"languageCode":"en_GB","languagePolicy":' \
                #            '"deterministic","master":true,"meta":' \
                #            '"{\\"example\\":\\"Hi [John], thank you for ' \
                #            'contacting Sendbee. How can we help you?\\"}",' \
                #            '"modifiedOn":1625843484807,"status":"PENDING",' \
                #            '"templateType":"TEXT","vertical":' \
                #            '"haw_can_we_help_you"}}'
                #     status_code = 200

                self.debug.ok(
                    constants.DebugConst.PARAMETERS,
                    self.parameters[constants.RequestConst.QUERY]
                )
                self.debug.ok(
                    constants.DebugConst.RESPONSE,
                    response
                )
                self.debug.set_curl(
                    constants.DebugConst.CURL,
                    response.request
                )

                return response.status_code, response.text

            else:
                return constants.ResponseCode.NOT_FOUND_404, {}

        def _process_response(self, status_code, response):
            """
            Process response using models
            :status_code: Response status code
            :response: Content
            :return: Response object
            """

            self.debug.ok(constants.DebugConst.STATUS_CODE, status_code)
            self.debug.ok(constants.DebugConst.RESPONSE, response)

            if not len(response) \
                    and \
                    status_code in constants.ResponseCode.ALLOW_EMPTY_RESPONSE:
                return constants.DefaultResponse.SUCCESS

            formatter = self.formatter
            if not formatter:
                formatter = FormatterFactory(constants.FormatterConst.JSON)\
                    .get_formatter()

            response = Response(response, status_code, formatter, self)
            formatted_data = response.formatted_data

            if status_code >= constants.ResponseCode.BAD_REQUEST_400:

                description = constants.ErrorConst.DEFAULT_DESCRIPTION

                try:
                    for key in constants.ErrorConst.DESCRIPTION_KEYS:
                        if formatted_data.get(key):
                            description = formatted_data.get(key)
                            break
                except (TypeError, AttributeError):
                    pass

                error_data = {
                    constants.ErrorConst.STATUS_KEY: status_code,
                    constants.ErrorConst.DESCRIPTION_KEY: description
                }

                self.debug.error(
                    constants.DebugConst.STATUS_CODE, status_code
                )
                self.debug.error(
                    constants.DebugConst.RESPONSE, response.formatted_data
                )
                raise RequestApiException(error_data)
            else:
                self.debug.ok(constants.DebugConst.STATUS_CODE, status_code)
                self.debug.ok(constants.DebugConst.RESPONSE, response.raw_data)

            if self.single_model_response:
                if response.models:
                    return response.models[0]
                else:
                    return None
            else:
                return response

        def call(self):
            """
            Makes the API call
            :return: Return value from self._process_response()
            """

            self.url = self._prepare_url()
            status_code, response = self._do_request(self.url)

            return self._process_response(status_code, response)

    def call(client, *path_params, **query_params):
        """
        Binded method for API calls
        :path_params: list of path parameters
        :query_params: dict of query parameters
        :return: Return value from Request.call()
        """

        if constants.MiscConst.PRINT_PARAMS in query_params:
            Request.query_parameters.print_params()
            return

        with Debug(client=client) as debug:
            request = Request(client, debug, *path_params, **query_params)
            return request.call()

    call.__doc__ = request_data.get(constants.ClientConst.DESCRIPTION)

    return call
