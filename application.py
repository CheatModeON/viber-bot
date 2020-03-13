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

app = Flask(__name__)

bot_configuration = BotConfiguration(
    name='CoronavirusLiveNews',
    avatar='https://www.zamzar.com/images/filetypes/doc.png',
    auth_token='4b352455f127dc7d-abf771323d3e435f-95efbc9daeaf7b85'
)
viber = Api(bot_configuration)

print(viber.get_account_info)

@app.route('/', methods=['POST'])
def incoming():
    #viber_request = viber.parse_request(request.get_data())

    #if isinstance(viber_request, ViberConversationStartedRequest) :
    #    viber.send_messages(viber_request.get_user().get_id(), [
    #        TextMessage(text="Welcome!")
    #    ])

    #return Response(status=200)
    return "test"


if __name__ == "__main__":
    #context = ('server.crt', 'server.key')
    #app.run(host='0.0.0.0', port=443, debug=True)
    app.run()
