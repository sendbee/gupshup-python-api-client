from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.messaging import query_params
from gupshup_python_api_client.messaging.models import SendMessageResponse, \
    MessageSeenResponse


class Messaging:
    """Api client for messaging"""

    send_message = bind_request(
        method=constants.RequestConst.POST,
        api_path='/wa/api/v1/msg',
        model=SendMessageResponse,
        force_single_model_response=True,
        query_parameters=query_params.SendMessage,
        default_parameters={
            'channel': 'whatsapp'
        },
        description='Send a WhatsApp message'
    )
    send_template_message = bind_request(
        method=constants.RequestConst.POST,
        api_path='/sm/api/v1/template/msg',
        model=SendMessageResponse,
        force_single_model_response=True,
        query_parameters=query_params.SendTemplateMessage,
        default_parameters={
            'channel': 'whatsapp'
        },
        description='Send a WhatsApp message template'
    )
    message_seen = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/wa/app/<app_id>/msg/<msg_id>/read',
        model=MessageSeenResponse,
        force_single_model_response=True,
        query_parameters=query_params.SendTemplateMessage,
        url_parameters=query_params.AppIdMsgIdInURL,
        description='Send a WhatsApp message template'
    )
