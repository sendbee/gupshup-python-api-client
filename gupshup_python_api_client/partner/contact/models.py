from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, BooleanField, \
    NumberField, ModelField


class Number(Model):
    """Data model for Gupshup contact number"""

    _active = BooleanField(index='active', desc='Is number active')
    _app_id = TextField(index='app_id', desc='UUID')
    _blocked = BooleanField(index='blocked', desc='Is number blocked')
    _country_code = NumberField(index='countryCode', desc='Number country code')
    _dial_code = NumberField(index='dialCode', desc='Number dial code')
    _phone_number = NumberField(index='phone', desc='Phone number')
    _status = TextField(index='status', desc='Number status')


class NumberStatus(Model):
    """Data model for Gupshup number status"""

    _number = ModelField(Number, index='userStatus',
                         desc='Contact phone number status')
