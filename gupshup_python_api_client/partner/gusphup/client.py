from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.gusphup import query_params
from gupshup_python_api_client.partner.gusphup.models import AppDailyDiscount, \
    WalletBalance


class Gupshup:
    """Partner Api client for gupshup platform"""

    daily_discount = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/discount',
        query_parameters=query_params.DailyDiscount,
        model=AppDailyDiscount,
        force_single_model_response=True,
        description='Gusphup app discounts'
    )

    wallet_balance = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/wallet/balance',
        query_parameters=query_params.WalletBalance,
        model=WalletBalance,
        force_single_model_response=True,
        description='Gusphup app wallet balance'
    )
