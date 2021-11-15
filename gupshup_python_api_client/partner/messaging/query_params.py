from gupshup_python_api_client.query_params import QueryParams


class ListTemplates(QueryParams):
    """Parameters for fetching a list of WhatsApp message templates"""

    app_id = 'app_id', 'Gupshup App ID'


class CreateTemplateURL(QueryParams):
    """URL Parameters for creating a WhatsApp message template"""

    app_id = 'app_id', 'Gupshup App ID'


class CreateTemplate(QueryParams):
    """Parameters for creating a WhatsApp message template"""

    element_name = 'elementName', 'Element name'
    language_code = 'languageCode', 'Language code'
    category = 'category', 'Template category'
    template_type = 'templateType', 'Template type'
    vertical = 'vertical', 'Same as element_name'
    content = 'content', 'Text body'
    example = 'example', 'Example text body'
    example_media = 'exampleMedia', 'Media Gupshup handle ID'
    buttons = 'buttons', 'Template buttons'


class UploadTemplateMedia(QueryParams):
    """Parameters for uploading template example media file"""

    file = 'file', 'File upload object'
    file_type = 'file_type', 'File mime type'
