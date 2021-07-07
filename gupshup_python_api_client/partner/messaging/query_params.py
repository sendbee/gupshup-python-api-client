from gupshup_python_api_client.query_params import QueryParams


class ListTemplates(QueryParams):
    """Parameters for fetching a list of WhatsApp message templates"""

    app_id = 'app_id', 'Gupshup App ID'


class CreateTemplate(QueryParams):
    """Parameters for creating a WhatsApp message template"""

    element_name = 'elementName', 'Gupshup App ID'
    language_code = 'languageCode', 'Gupshup App ID'
    category = 'category', 'Gupshup App ID'
    template_type = 'templateType', 'Gupshup App ID'
    vertical = 'vertical', 'Gupshup App ID'
    content = 'content', 'Gupshup App ID'
    buttons = 'buttons', 'Gupshup App ID'
