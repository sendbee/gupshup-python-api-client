from gupshup_python_api_client.query_params import QueryParams


class Number(QueryParams):
    """Query parameters for getting partner token"""

    app_id = 'app_id', 'Gupshup APP UUID'
    number = 'phone', 'Contact phone number'
