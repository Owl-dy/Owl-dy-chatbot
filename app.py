import os, sys
from flask import Flask, request
from pymessenger import Bot
from utils import wit_response, talk_back

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "Token For Facebook Webhook"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']
                
                # If received text message
				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					break_down = wit_response(messaging_text)
					print (break_down)
					elements = talk_back(break_down)
					print (elements)

					#if the talk back returns a string, package it as a return then send back
					if isinstance(elements, str):
						bot.send_text_message(sender_id, elements)
					#if a service is requested, the talk back will return a botton object. Here, package it in a botton template then send back
					else:
						bot.send_button_message(sender_id,'Owl-dy, let me help you: ',elements)
					


					# Echo
					#response = messaging_text
					#bot.send_text_message(sender_id, response)

	return "ok", 200

def log(message):
	#print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)
