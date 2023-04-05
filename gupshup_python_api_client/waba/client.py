from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.waba import query_params
from gupshup_python_api_client.waba.models import ProfileDetails


class Waba:
    """Api client for waba account"""

    waba_account = bind_request(
        method=constants.RequestConst.GET,
        api_path='/wa/app/<app_id>/business/profile/waba',
        model=ProfileDetails,
        force_single_model_response=True,
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.AppIdInURL,
        description='Get WABA profile data'
    )
