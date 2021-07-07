from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.messaging import query_params
from gupshup_python_api_client.partner.messaging.models import TemplateList, \
    Template


class Messaging:
    """Api client for messaging"""

    list_templates = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/templates',
        header={'Connection': 'keep-alive'},
        force_single_model_response=True,
        model=TemplateList,
        query_parameters=query_params.ListTemplates,
        description='Get WhatsApp message template list'
    )

    create_template = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/app/<app_id>/templates',
        header={'Connection': 'keep-alive'},
        force_single_model_response=True,
        model=Template,
        query_parameters=query_params.CreateTemplate,
        description='Create WhatsApp message template'
    )
