from gupshup_python_api_client.query_params import QueryParams


class PartnerToken(QueryParams):
    """Query parameters for getting partner token"""

    email = 'email', 'Account email address'
    password = 'password', 'Account password'


class AppToken(QueryParams):
    """Query parameters for getting partner APP token"""

    app_id = 'app_id', 'Gupshup APP ID'
