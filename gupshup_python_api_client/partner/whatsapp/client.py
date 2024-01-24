from gupshup_python_api_client import constants
from gupshup_python_api_client.bind import bind_request
from gupshup_python_api_client.partner.whatsapp import query_params
from gupshup_python_api_client.partner.whatsapp.models import ProfileDetails, \
    AboutText, RequestStatus


class Whatsapp:
    """Partner Api client for WABA accounts"""

    whatsapp_profile = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/business/profile',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.Profile,
        model=ProfileDetails,
        force_single_model_response=True,
        description='Get WABA profile data'
    )

    update_whatsapp_profile = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/business/profile',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.ProfileUpdate,
        model=ProfileDetails,
        force_single_model_response=True,
        description='Update WABA profile data'
    )

    get_whatsapp_about = bind_request(
        method=constants.RequestConst.GET,
        api_path='/partner/app/<app_id>/business/profile/about',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.Profile,
        model=AboutText,
        force_single_model_response=True,
        description='Get WABA profile about text'
    )

    update_whatsapp_about = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/business/profile/about',
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.ProfileAbout,
        model=AboutText,
        force_single_model_response=True,
        description='Update WABA profile about text'
    )

    update_whatsapp_profile_picture = bind_request(
        method=constants.RequestConst.PUT,
        api_path='/partner/app/<app_id>/business/profile/photo',
        header={
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data'
        },
        url_parameters=query_params.AppIdInURL,
        query_parameters=query_params.ProfileAbout,
        file_parameters=query_params.UploadProfilePhotoFile,
        model=RequestStatus,
        force_single_model_response=True,
        description='Update WABA profile photo'
    )

    delete_whatsapp_profile_picture = bind_request(
        method=constants.RequestConst.DELETE,
        api_path='/partner/app/<app_id>/business/profile/photo',
        url_parameters=query_params.AppIdInURL,
        model=RequestStatus,
        force_single_model_response=True,
        description='Delete WABA profile photo'
    )
