from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, BooleanField, \
    ModelField, TimestampField, JsonField


class Template(Model):
    """Data model for Gupshup WhatsApp message template"""

    _id = TextField(index='id', desc='UUID')
    _created_at = TimestampField(index='createdOn', desc='Template created at')
    _modified_at = TimestampField(
        index='modifiedOn', desc='Template modified at')
    _category = TextField(index='category', desc='Message category')
    _body = TextField(index='data', desc='Message body')
    _keyword = TextField(index='elementName', desc='Template keyword')
    _language = TextField(index='languageCode', desc='Template language')
    _language_policy = TextField(
        index='languagePolicy', desc='Template language policy')
    _master = BooleanField(index='master', desc='Is template master')
    _meta = JsonField(index='meta', desc='Template meta')
    _status = TextField(index='status', desc='Template status')
    _type = TextField(index='templateType', desc='Template type')
    _vertical = TextField(index='vertical', desc='Template vertical')
    _rejected_reason = TextField(
        index='reason', desc='Template rejected reason')


class TemplateList(Model):
    """Data model for Gupshup WhatsApp message template list"""

    _status = TextField(index='status', desc='Request status')
    _templates = ModelField(
        Template, index='templates',
        desc='Gupshup WhatsApp Message template list')


class CreateTemplate(Model):
    """Data model for Gupshup WhatsApp message template created"""

    _status = TextField(index='status', desc='Request status')
    _message = TextField(index='message', desc='Error message')
    _template = ModelField(
        Template, index='template',
        desc='Gupshup WhatsApp Message template')


class MediaHandleMessageID(Model):
    """Data model for Gupshup uploaded media handle message id"""

    _message = TextField(index='message', desc='Media handle ID')


class MediaHandle(Model):
    """Data model for Gupshup uploaded media handle"""

    _handle = ModelField(MediaHandleMessageID,
                         index='handleId', desc='Media handle ID')
    _status = TextField(index='status', desc='Request status')


class SendMessageResponse(Model):
    """Data model for sent message"""

    _status = TextField(index='status', desc='Message status')
    _message_id = TextField(index='messageId', desc='Message UUID')
