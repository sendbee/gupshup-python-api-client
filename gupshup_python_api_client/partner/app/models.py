from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, BooleanField, \
    ModelField, TimestampField, NumberField


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


class AppHealth(Model):
    """Data model for Gupshup app health"""

    _healthy = BooleanField(index='healthy', desc='Healthy or not')


class AppRating(Model):
    """Data model for Gupshup app rating"""

    _message_limit = NumberField(
        index='currentLimit', desc='Max number of message per day')
    _event = TextField(
        index='event', desc='Tier change event')
    _event_time = TimestampField(
        index='eventTime', desc='Event time')
    _old_limit = TimestampField(
        index='oldLimit', desc='Previous messaging limit')


class WebhookURL(Model):
    """Data model for Gupshup webhook url"""

    _success = TextField(
        index='success', desc='Action success')


class WebhookEvent(Model):
    """Data model for Gupshup webhook event"""

    _success = TextField(
        index='success', desc='Action success')


class OptinMessage(Model):
    """Data model for Gupshup webhook url"""

    _success = TextField(
        index='success', desc='Action success')


class EnablingTemplateMessaging(Model):
    """Data model for Gupshup enabling/disabling template messaging"""

    _success = TextField(
        index='success', desc='Action success')
