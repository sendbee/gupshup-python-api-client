from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.auth import query_params
from gupshup_python_api_client.partner.auth.models import PartnerToken, AppToken


class Auth:
    """Partner Api client for authentication"""

    partner_token = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/account/login',
        header={
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        query_parameters=query_params.PartnerToken,
        model=PartnerToken,
        description='Get partner API token',
        payload_format=constants.RequestConst.PARAMS_URL_ENCODED
    )

    app_token = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/token',
        query_parameters=query_params.AppToken,
        model=AppToken,
        force_single_model_response=True,
        description='Get partner API APP token'
    )
