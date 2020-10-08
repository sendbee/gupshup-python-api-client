from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.contacts.models import OptInResponse
from gupshup_python_api_client.contacts import query_params


class Contacts:
    """Api client for contacts"""

    opt_in = bind_request(
        method=constants.RequestConst.POST,
        api_path='/sm/api/v1/app/opt/in',
        path=['app_name'],
        query_parameters=query_params.OptIn,
        model=OptInResponse,
        description='Opt-in a user (phone number) via API'
    )
