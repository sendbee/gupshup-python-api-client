from gupshup_api import constants


class Response:
    """Response object returned from API call."""

    def __init__(self, data, status_code, formatter, api_request):
        self._data = data
        self._model = api_request.model

        self.api_reguest = api_request
        self.formatter = formatter(self)
        self.status_code = status_code

        self._response_data = {
            constants.FormatterConst.FORMATTED: None,
            constants.ClientConst.MODELS: None,
        }

    def __iter__(self):
        return iter(self.models)

    @property
    def raw_data(self):
        """Return data as is from the server."""

        return self._data

    @property
    def formatted_data(self):
        """Format data using selected formatter."""

        if self._response_data[constants.FormatterConst.FORMATTED] is None:
            self._response_data[constants.FormatterConst.FORMATTED] = \
                self.formatter.format_data(self._data)

        return self._response_data[constants.FormatterConst.FORMATTED]

    @property
    def models(self):
        """Transform raw data into models."""

        if not self._response_data[constants.ClientConst.MODELS]:
            formatted_data = self.formatter.format_data(self._data)
            if not isinstance(formatted_data, list):
                formatted_data = [formatted_data]
            self._response_data[constants.ClientConst.MODELS] = \
                self._model.process(formatted_data)

        return self._response_data[constants.ClientConst.MODELS]
