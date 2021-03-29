from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, BooleanField, \
    NumberField, ModelField, TimestampField


class PartnerToken(Model):
    """Data model for partner token response"""

    _id = NumberField(index='id', desc='Account id')
    _admin = BooleanField(index='admin', desc='Account admin')
    _name = TextField(index='name', desc='Account name')
    _terms_read = BooleanField(index='terms_read', desc='Terms are read')
    _token = TextField(index='token', desc='Partner API token')


class Token(Model):
    """Data model for partner APP token response"""

    _active = BooleanField(index='active', desc='Token active')
    _authoriser_id = TextField(index='authoriserId', desc='Token authoriser ID')
    _requestor_id = TextField(index='requestorId', desc='Token requestor ID')
    _created_at = TimestampField(index='createdOn', desc='Token created at')
    _expires_at = TimestampField(index='expiresOn', desc='Token expires at')
    _modified_at = TimestampField(index='modifiedOn', desc='Token modified at')
    _token = TextField(index='token', desc='Partner API APP token')


class AppToken(Model):
    """Data model for partner APP parent token response"""

    _status = TextField(index='status', desc='Request status')
    _token = ModelField(Token, index='token', desc='Token data')
