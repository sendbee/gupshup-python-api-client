import ujson
from datetime import datetime

from gupshup_python_api_client import constants


class Field:
    """Abstract field class."""

    def __init__(self, index, desc=None, **kwargs):
        self.index = index
        self._kwargs = kwargs

        self.__doc__ = desc
        self.value = None

    def convert_item(self, model):
        """Convert item to desired item type"""

        try:
            self.value = model.item[self.index]
        except IndexError:
            self.value = None
        except KeyError:
            self.value = None

        try:
            if self.value is not None:
                self.value = self._convert_field_item(
                    self.value, **self._kwargs
                )
        except TypeError:
            self.value = None

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        return data


class NumberField(Field):
    """Converting item to integer."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            return int(data)
        except ValueError:
            return 0


class RealNumberField(Field):
    """Converting item to integer."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            return float(data)
        except ValueError:
            return 0.0


class TextField(Field):
    """Converting item to string."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            return str(data)
        except ValueError:
            return ''


class JsonField(Field):
    """Converting json to object."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            return ujson.loads(data)
        except ValueError:
            return ''


class BooleanField(Field):
    """Converting item to boolean."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        return bool(data)


class DatetimeField(Field):
    """Converting item to datetime object."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            _format = kwargs.get(constants.MiscConst.FORMAT)
            return datetime.strptime(data, _format)
        except ValueError:
            return data


class TimestampField(Field):
    """Converting item to datetime object."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            _format = kwargs.get(constants.MiscConst.FORMAT)
            return datetime.strptime(datetime.fromtimestamp(data), _format)
        except ValueError:
            return data


class ListField(Field):
    """Converting item to list."""

    def _convert_field_item(self, data, **kwargs):
        """Actual converting."""

        try:
            return list(data)
        except ValueError:
            return data


class ModelField(Field):
    """Converting item to another data model."""

    def __init__(self, model_cls, index, desc=None, **kwargs):
        self.model_cls = model_cls
        super().__init__(index, desc, **kwargs)
