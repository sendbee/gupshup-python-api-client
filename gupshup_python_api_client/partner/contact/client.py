from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.contact import query_params
from gupshup_python_api_client.partner.contact.models import NumberStatus


class Contact:
    """Partner Api client for contacts"""

    number = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/userStatus',
        header={'Connection': 'keep-alive'},
        query_parameters=query_params.Number,
        model=NumberStatus,
        force_single_model_response=True,
        description='Get partner API number status'
    )
