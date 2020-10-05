from gupshup_api.models import Model
from gupshup_api.fields import TextField


class SendMessageResponse(Model):
    """Data model for opt-in response"""

    _status = TextField(index='status', desc='Message status')
    _message_id = TextField(index='messageId', desc='Message UUID')
