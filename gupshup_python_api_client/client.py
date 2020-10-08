import click

from gupshup_python_api_client.contacts.client import Contacts
from gupshup_python_api_client.messaging.client import Messaging
from gupshup_python_api_client.exceptions import RequestApiException


class Client(Contacts, Messaging):
    """Main API class. Sets all API calls."""
    base_url = 'api.gupshup.io'
    protocol = 'https'

    def __init__(self, api_key, debug=False, fake_response_path=None):

        if not api_key:
            raise RequestApiException('API key missing!')

        self.debug = debug
        self.request = None
        self.api_key = api_key
        self.fake_response_path = fake_response_path

    @classmethod
    def print_params_for(cls, fn_name) -> None:
        """Prints parameters for certain API call function."""

        try:
            getattr(cls, fn_name)(None, print_params=True)
        except AttributeError:
            click.secho('Unknown API method: {}'.format(fn_name), fg='red')

