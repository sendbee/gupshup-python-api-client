from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.onboarding import query_params
from gupshup_python_api_client.partner.onboarding.models import \
    CreatedApp, ContactDataAdded, CallbackUrlAdded, VerificationEmailResent, \
    OnboardingLinkGenerated


class Onboarding:
    """Partner Api client for onboarding apps"""

    create_app = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/app',
        query_parameters=query_params.CreateApp,
        model=CreatedApp,
        force_single_model_response=True,
        description='Create APP'
    )

    set_callback_url = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/callback',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.SetCallbackUrl,
        model=CallbackUrlAdded,
        force_single_model_response=True,
        description='Set callback url'
    )

    add_contact_data = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/onboarding/contact',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.AddContactData,
        model=ContactDataAdded,
        force_single_model_response=True,
        description='Add contact data'
    )

    resend_verification_email = bind_request(
        method=constants.RequestConst.POST,
        api_path='/partner/app/<app_id>/onboarding/contact/email/resend',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.ResendVerificationEmail,
        model=VerificationEmailResent,
        force_single_model_response=True,
        description='Resend verification email'
    )

    generate_onboarding_link = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/onboarding/embed/link',
        query_parameters=query_params.GenerateOnboardingLink,
        model=OnboardingLinkGenerated,
        force_single_model_response=True,
        description='Generate onboarding link'
    )
