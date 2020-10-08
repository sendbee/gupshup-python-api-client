from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField


class SendMessageResponse(Model):
    """Data model for opt-in response"""

    _status = TextField(index='status', desc='Message status')
    _message_id = TextField(index='messageId', desc='Message UUID')
