import ujson

from abc import ABCMeta, abstractmethod

from gupshup_api import constants


class Formatter(metaclass=ABCMeta):
    """Abstract formatter class."""

    def __init__(self, response):
        self._response = response

    @abstractmethod
    def _format_data(self, data):
        """Format method in formatter classes."""

        return data

    def format_data(self, data):
        """Main format method."""

        return self._format_data(data)


class Json(Formatter):
    """JSON data formatter class. Accepts empty response as well"""

    def _unpack_response(self, data):
        """JSON decode"""
        if not data:
            return ''

        try:
            return ujson.loads(data)
        except ValueError:
            return constants.DefaultResponse.INVALID_RESPONSE

    def _format_data(self, data):
        """Transform raw data from server into python native type."""

        return self._unpack_response(data)


class FormatterFactory:
    """Formatter factory class."""

    formatters = {
        constants.FormatterConst.JSON: Json,
    }

    def __init__(self, name: str):
        self._name = name

    def get_formatter(self):
        """Get the formatter class using string key."""

        return FormatterFactory.formatters.get(self._name)
