from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import requests

app = Flask(__name__)

bot_configuration = BotConfiguration(
    name='CoronavirusLiveNews',
    avatar='https://www.zamzar.com/images/filetypes/doc.png',
    auth_token='4b352455f127dc7d-abf771323d3e435f-95efbc9daeaf7b85'
)
viber = Api(bot_configuration)

@app.route('/', methods=['GET'])
def incoming():
    #viber_request = viber.parse_request(request.get_data())

    #if isinstance(viber_request, ViberConversationStartedRequest) :
    #    viber.send_messages(viber_request.get_user().get_id(), [
    #        TextMessage(text="Welcome!")
    #    ])
    
    url = 'https://chatapi.viber.com/pa/send_message'
    data = {
        "receiver": "5419277678147001469",
        "type": "text",
        "text": "Hello world!"
    }
    headers = {
    "Content-Type", "application/application/json",
    "X-Viber-Auth-Token", "4b352455f127dc7d-abf771323d3e435f-95efbc9daeaf7b85"
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)


    return Response(status=200)


if __name__ == "__main__":
    #context = ('server.crt', 'server.key')
    #app.run(host='0.0.0.0', port=443, debug=True)
    app.run()
