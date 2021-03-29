from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.app import query_params
from gupshup_python_api_client.partner.app.models import AppList


class App:
    """Partner Api client for Gupshup apps"""

    list_apps = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/account/api/partnerApps',
        query_parameters=query_params.AppList,
        model=AppList,
        force_single_model_response=True,
        description='Get partner API APP list'
    )
