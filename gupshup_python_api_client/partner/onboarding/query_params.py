from gupshup_python_api_client.query_params import QueryParams


class AppIdInURL(QueryParams):
    """URL Parameters for app_id in url"""

    app_id = 'app_id', 'Gupshup App ID'


class CreateApp(QueryParams):
    """Body parameters for creating app"""

    name = 'name', 'APP name'
    template_messaging = 'templateMessaging', 'WA template messaging on/off'
    disable_optin_url = 'disableOptinPrefUrl', 'Disable optin msg'


class AddContactData(QueryParams):
    """Body parameters for adding app's contact data"""

    email = 'contactEmail', 'Email address'
    name = 'contactName', 'Contact name'
    phone_number = 'contactNumber', 'Contact phone number'


class SetCallbackUrl(QueryParams):
    """Body parameters for setting app's callback url"""

    url = 'url', 'Callback url'
    events = 'modes', 'NONE,READ,DELIVERED,SENT,DELETED,OTHERS'
    direct_forwarding = 'directForwarding', \
                        'boolean value which is true if the events to be ' \
                        'sent directly and false if the events need to to ' \
                        'send via platform'
    notify_via_phone = 'notifyWithPhone', \
                       'boolean value which is true if the events should ' \
                       'contain the source phone number. false otherwise'


class ResendVerificationEmail(QueryParams):
    """Resend verification email message"""


class GenerateOnboardingLink(QueryParams):
    """Generate onboarding link"""

    app_id = 'app_id', 'Gupshup App ID'
    regenerate = 'regenerate', 'true|false'
    username = 'user', 'FB manager username'
    language = 'lang', 'Supported language'
