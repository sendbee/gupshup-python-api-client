from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField


class CreatedApp(Model):
    """Created app data model"""

    _app_id = TextField(index='appId', desc='UUID')


class ContactDataAdded(Model):
    """Contact data added data model"""


class CallbackUrlAdded(Model):
    """Callback url data model"""


class VerificationEmailResent(Model):
    """Verification email data model"""


class OnboardingLinkGenerated(Model):
    """Onboarding link data model"""

    link = 'link', 'Onboarding link'
