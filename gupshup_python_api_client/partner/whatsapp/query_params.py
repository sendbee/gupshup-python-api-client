from gupshup_python_api_client.query_params import QueryParams


class AppIdInURL(QueryParams):
    """URL Parameters for app_id in url"""

    app_id = 'app_id', 'Gupshup App ID'


class Profile(QueryParams):
    """URL Parameters for WABA profile"""

    app_id = 'app_id', 'Gupshup App ID'


class ProfileUpdate(QueryParams):
    """Query parameters for WABA profile update"""

    address1 = 'addLine1', 'WABA profile address1'
    address2 = 'addLine2', 'WABA profile address2'
    city = 'city', 'WABA profile city'
    state = 'state', 'WABA profile state'
    country = 'country', 'WABA profile country'
    zip_code = 'pinCode', 'WABA profile zip code'
    email = 'profileEmail', 'WABA profile email'
    description = 'desc', 'WABA profile description'
    vertical = 'vertical', 'WABA profile vertical'
    website1 = 'website1', 'WABA profile website 1'
    website2 = 'website2', 'WABA profile website 2'


class ProfileAbout(QueryParams):
    """Query parameters for WABa profile about update"""

    about = 'about', 'WABA profile about'


class UploadProfilePhotoFile(QueryParams):
    """Parameters for uploading template example media file"""

    file = 'file', 'File upload object'
