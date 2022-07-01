from gupshup_python_api_client.query_params import QueryParams


class DailyDiscount(QueryParams):
    """Query parameters for app's daily discounts"""

    year = 'year', 'Year'
    month = 'month', 'Month'
    app_id = 'app_id', 'Gupshup App ID'


class WalletBalance(QueryParams):
    """Query parameters for app's wallet balance"""

    app_id = 'app_id', 'Gupshup App ID'
