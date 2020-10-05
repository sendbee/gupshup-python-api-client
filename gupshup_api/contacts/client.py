from gupshup_api import constants
from gupshup_api.bind import bind_request
from gupshup_api.contacts.models import OptInResponse
from gupshup_api.contacts import query_params


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
