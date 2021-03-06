from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, BooleanField, \
    ModelField, TimestampField


class App(Model):
    """Data model for Gupshup app"""

    _id = TextField(index='id', desc='UUID')
    _created_at = TimestampField(index='createdOn', desc='Token created at')
    _healthy = BooleanField(index='healthy', desc='Is app healthy')
    _live = BooleanField(index='live', desc='Is app live')
    _stopped = BooleanField(index='stopped', desc='Is app stoped')
    _modified_at = TimestampField(index='modifiedOn', desc='Token modified at')
    _name = TextField(index='name', desc='App name')
    _partner_id = TextField(index='partnerId', desc='Partner ID')
    _phone_number = TextField(index='phone', desc='App phone number')


class AppList(Model):
    """Data model for Gupshup app list"""

    _apps = ModelField(App, index='partnerAppsList', desc='Gupshup app list')
