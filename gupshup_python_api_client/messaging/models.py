from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, JsonField


class SendMessageResponse(Model):
    """Data model for sent message"""

    _status = TextField(index='status', desc='Message status')
    _message = TextField(index='message', desc='Fail message')
    _invalid_constraint_information = JsonField(
        index='invalidConstraintInformation', desc='Invalid message'
    )
    _message_id = TextField(index='messageId', desc='Message UUID')
