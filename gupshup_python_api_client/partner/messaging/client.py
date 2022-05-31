from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.messaging import query_params
from gupshup_python_api_client.partner.messaging.models import TemplateList, \
    CreateTemplate, MediaHandle, SendMessageResponse


class Messaging:
    """Api client for messaging"""

    list_templates = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/templates',
        header={'Connection': 'keep-alive'},
        force_single_model_response=True,
        model=TemplateList,
        query_parameters=query_params.AppIdInURL,
        description='Get WhatsApp message template list'
    )

    upload_template_example_media = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/app/<app_id>/upload/media',
        header={'Connection': 'keep-alive'},
        force_single_model_response=True,
        model=MediaHandle,
        query_parameters=query_params.UploadTemplateMedia,
        file_parameters=query_params.UploadTemplateMediaFile,
        url_parameters=query_params.AppIdInURL,
        description='Upload template example media file'
    )

    create_template = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/app/<app_id>/templates',
        header={'Connection': 'keep-alive'},
        force_single_model_response=True,
        model=CreateTemplate,
        query_parameters=query_params.CreateTemplate,
        url_parameters=query_params.AppIdInURL,
        description='Create WhatsApp message template'
    )

    send_template_message = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/app/<app_id>/template/msg',
        header={'Connection': 'keep-alive'},
        force_single_model_response=True,
        model=SendMessageResponse,
        query_parameters=query_params.SendTemplateMessage,
        url_parameters=query_params.AppIdInURL,
        description='Send a WhatsApp message template'
    )
