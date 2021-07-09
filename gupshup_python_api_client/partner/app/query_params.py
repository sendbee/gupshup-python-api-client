from gupshup_python_api_client.query_params import QueryParams


class AppList(QueryParams):
    """Query parameters for getting partner token"""


class AppHealth(QueryParams):
    """Query parameters for getting app health"""

    app_id = 'app_id', 'Gupshup App ID'


class AppRatings(QueryParams):
    """Query parameters for getting app ratings"""

    app_id = 'app_id', 'Gupshup App ID'
