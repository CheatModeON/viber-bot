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


@app.route('/', methods=['POST'])
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

    #r = requests.post(url, data=json.dumps(data), headers=headers)

    #return Response(status=200)
    
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            message
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)


if __name__ == "__main__":
    #context = ('server.crt', 'server.key')
    #app.run(host='0.0.0.0', port=443, debug=True)
    app.run()
