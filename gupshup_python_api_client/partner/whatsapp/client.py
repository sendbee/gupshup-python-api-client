from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.whatsapp import query_params
from gupshup_python_api_client.partner.whatsapp.models import ProfileDetails


class Whatsapp:
    """Partner Api client for WABA accounts"""

    update_whatsapp_profile = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/business/profile',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.ProfileUpdate,
        model=ProfileDetails,
        force_single_model_response=True,
        description='Update WABA profile data'
    )
