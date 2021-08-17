from gupshup_python_api_client.query_params import QueryParams


class SendMessage(QueryParams):
    """Parameters for sending a WhatsApp message"""

    source = 'source', 'Source Phone number'
    destination = 'destination', 'Destination phone number'
    message = 'message', 'Message text or json-encoded data'
    src_name = 'src.name', 'Optional, for Sandbox apps only'


class SendTemplateMessage(QueryParams):
    """Parameters for sending a WhatsApp message template"""

    source = 'source', 'Source Phone number'
    destination = 'destination', 'Destination phone number'
    template = 'template', 'Template data'
    message = 'message', 'Message data'
