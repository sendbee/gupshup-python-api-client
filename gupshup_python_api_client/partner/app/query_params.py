from gupshup_python_api_client.query_params import QueryParams


class AppIdInURL(QueryParams):
    """URL Parameters for app_id in url"""

    app_id = 'app_id', 'Gupshup App ID'


class AppList(QueryParams):
    """Query parameters for getting partner token"""


class AppHealth(QueryParams):
    """Query parameters for getting app health"""

    phone = 'phone', 'App phone number'
    is_blocked = 'isBlocked', 'Is app blocked'


class AppRatings(QueryParams):
    """Query parameters for getting app ratings"""

    app_id = 'app_id', 'Gupshup App ID'


class WebhookURL(QueryParams):
    """Query parameters for setting webhook url"""

    url = 'callbackUrl', 'Webhook URL'


class OptinMessage(QueryParams):
    """Query parameters for setting automated optin message"""

    enable = 'enableOptinMessage', 'True|False'


class WebhookEvents(QueryParams):
    """Query parameters for setting webhook events"""

    events = 'modes', 'DELIVERED|READ|SENT|DELETED|OTHERS|TEMPLATE|ACCOUNT'


class EnableTemplateMessaging(QueryParams):
    """Query parameters for enabling/disabling template messaging"""

    enable = 'isHSMEnabled', 'True|False'


class AppUsage(QueryParams):
    """Query parameters for fetching app usages"""

    app_id = 'app_id', 'Gupshup App ID'
    date_from = 'from', 'YYYY-MM-DD from'
    date_to = 'to', 'YYYY-MM-DD to'
