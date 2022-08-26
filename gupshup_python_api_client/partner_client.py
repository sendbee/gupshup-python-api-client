import click

from gupshup_python_api_client.partner.app.client import App
from gupshup_python_api_client.partner.auth.client import Auth
from gupshup_python_api_client.partner.contact.client import Contact
from gupshup_python_api_client.partner.gusphup.client import Gupshup
from gupshup_python_api_client.partner.whatsapp.client import Whatsapp
from gupshup_python_api_client.partner.messaging.client import Messaging


class PartnerClient(Auth, App, Contact, Messaging, Gupshup, Whatsapp):
    """Partner API class. Sets all Partner API calls."""

    base_url = 'partner.gupshup.io'
    protocol = 'https'

    def __init__(self, token=None, authorization=None, debug=False,
                 fake_response_path=None):

        self.debug = debug
        self.request = None
        self.api_key = None
        self.api_token = token
        self.api_authorization = authorization
        self.fake_response_path = fake_response_path

    @classmethod
    def print_params_for(cls, fn_name) -> None:
        """Prints parameters for certain API call function."""

        try:
            getattr(cls, fn_name)(None, print_params=True)
        except AttributeError:
            click.secho('Unknown API method: {}'.format(fn_name), fg='red')

