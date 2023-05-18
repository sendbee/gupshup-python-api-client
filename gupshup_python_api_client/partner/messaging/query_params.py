from gupshup_python_api_client.query_params import QueryParams


class AppIdInURL(QueryParams):
    """URL Parameters for app_id in url"""

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
    media_handle_id = 'exampleMedia', 'Media Gupshup handle ID'
    enable_sample = 'enableSample', 'Enable example media'
    buttons = 'buttons', 'Template buttons'
    template_change = 'allowTemplateCategoryChange', 'Dynamic template change'


class UploadTemplateMedia(QueryParams):
    """Parameters for uploading template example media file"""

    file_type = 'file_type', 'File mime type'


class UploadTemplateMediaFile(QueryParams):
    """Parameters for uploading template example media file"""

    file = 'file', 'File upload object'


class SendTemplateMessage(QueryParams):
    """Parameters for sending a WhatsApp message template"""

    source = 'source', 'Source Phone number'
    sandbox = 'sandbox', 'Send in sandbox mode'
    destination = 'destination', 'Destination phone number'
    template = 'template', 'Template data'
    message = 'message', 'Message data'
    app_name = 'src.name', 'Gupshup app name'
