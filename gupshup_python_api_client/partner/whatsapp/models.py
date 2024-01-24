from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, ModelField


class Profile(Model):
    """Data model for partner WABA profile details"""

    _address = TextField(index='addressLine1', desc='WABA profile address')
    _email = TextField(index='profileEmail', desc='WABA profile email')
    _description = TextField(index='desc', desc='WABA profile description')
    _vertical = TextField(index='vertical', desc='WABA profile vertical')
    _website1 = TextField(index='website1', desc='WABA profile 1')
    _website2 = TextField(index='website2', desc='WABA profile 2')


class ProfileDetails(Model):
    """Data model for partner WABA profile data submit"""

    _status = TextField(index='status', desc='Request status')
    _profile = ModelField(Profile, index='profile', desc='WABA profile details')


class About(Model):
    """Data model for partner WABA profile about"""

    _text = TextField(index='message', desc='WABA profile about text')


class AboutText(Model):
    """Data model for partner WABA profile about text"""

    _status = TextField(index='status', desc='Request status')
    _about = ModelField(About, index='about', desc='WABA profile details')


class RequestStatus(Model):
    """Data model for partner WABA request status"""

    _status = TextField(index='status', desc='Request status')
    _message = TextField(index='message', desc='Request message')
