from gupshup_api import constants
from gupshup_api.bind import bind_request
from gupshup_api.messaging.models import SendMessageResponse
from gupshup_api.messaging import query_params


class Messaging:
    """Api client for automation"""

    send_message = bind_request(
        method=constants.RequestConst.POST,
        api_path='/sm/api/v1/msg',
        model=SendMessageResponse,
        force_single_model_response=True,
        query_parameters=query_params.SendMessage,
        default_parameters={
            'channel': 'whatsapp'
        },
        description='Send a WhatsApp message'
    )
