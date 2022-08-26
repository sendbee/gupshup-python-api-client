from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.app import query_params
from gupshup_python_api_client.partner.app.models import \
    AppList, AppHealth, AppRating, WebhookURL, OptinMessage, WebhookEvent, \
    EnablingTemplateMessaging, AppUsageList


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

    app_health = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/health',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.AppHealth,
        model=AppHealth,
        force_single_model_response=True,
        description='Get partner API APP health'
    )

    app_rating = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/ratings',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.AppRatings,
        model=AppRating,
        force_single_model_response=True,
        description='Get partner API APP rating'
    )

    set_webhook_url = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/callbackURL',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.WebhookURL,
        model=WebhookURL,
        description='Set webhook URl for the app'
    )

    set_automated_optin_message = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/optinMessagePreference',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.OptinMessage,
        model=OptinMessage,
        description='Set automated optin message'
    )

    webhook_events = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/callback/mode',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.WebhookEvents,
        model=WebhookEvent,
        description='Set webhook events'
    )

    enable_template_messaging = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/appPreference',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.EnableTemplateMessaging,
        model=EnablingTemplateMessaging,
        description='Enabling/disabling template messaging'
    )

    app_usage = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/usage',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.AppUsage,
        force_single_model_response=True,
        model=AppUsageList,
        description='App usage'
    )

