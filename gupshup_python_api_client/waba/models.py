from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, ModelField


class Profile(Model):
    """Data model for partner WABA profile details"""

    _business_name = TextField(index='businessName', desc='WABA business name')
    _display_name = TextField(index='displayName', desc='WABA display name')
    _phone_number = TextField(index='phoneNumber', desc='WABA phone number')
    _timezone = TextField(index='timeZone', desc='WABA timezone')
    _waba_id = TextField(index='wabaId', desc='WABA ID')


class ProfileDetails(Model):
    """Data model for partner WABA profile data"""

    _status = TextField(index='status', desc='Request status')
    _profile = ModelField(Profile, index='profileWabaDetails',
                          desc='WABA profile details')
