# gupshup-python-api-client

## Table of contents  

-   [Installation](#installation)
-   [Initialization](#initialization)

#### Messaging

-   [Opt-in user](#opt-in-user)
-   [Send a message](#send-message)

---

### <a name='installation'>Installation</a>

Register git repository as a dependency in your project

```yaml
git+ssh://git@github.com/sendbee/gupshup-python-api-client.git@master
```


### <a name='initialization'>Initialization</a>

```python
from gupshup_python_api_client import GupshupApi

api = GupshupApi('__your_api_key_here__')
```

### <a name='opt-in-user'>Opt-in user</a>

```python
from gupshup_python_api_client import GupshupApi


api_key = '__your_api_key_here__'
app_name = '__your_gupshup_app_name_here__'

api = GupshupApi(api_key)

response = api.opt_in(app_name, user='phone_number')

response.status
```

### <a name='send-message'>Send a message</a>

For supported message types and data, see
[Gupshup documentation](https://www.gupshup.io/developer/docs/bot-platform/guide/whatsapp-api-documentation#OutboundMessage)


```python
from gupshup_python_api_client import GupshupApi
import ujson as json


api_key = '__your_api_key_here__'

api = GupshupApi(api_key)

# example text message
text_message = {
    'isHSM': False,
    "type": "text",
    "text": "sample text message"
}
# example image message
image_message = {
    "type": "image",
    "originalUrl": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg",
    "previewUrl": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg",
    "caption":"Sample image"
}
# example file message
file_message = {
    "type": "file",
    "url": "http://enterprise.smsgupshup.com/doc/GatewayAPIDoc.pdf",
    "filename": "Sample file"
}
# example audio message
audio_message = {
    "type": "audio",
    "url": "https://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_700KB.mp3"
}

source_number = '__your_whatsapp_business_number__'
destination_number = '__contact_phone_number__'

# JSON-encode the desired message 
message_payload = json.dumps(text_message)
response = api.send_message(
    source=source_number,
    destination=destination_number,
    message=message_payload
)

response.status
response.message_id
```
