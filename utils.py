from wit import Wit 
import random

'''
This code is utilized in a chatbot, which is built for a class project by Tom Fu

'''


cheer = {
'baker': ['Baker is the most conveniently located college!','BAKER COMES FIRST!', 'Baker Loves Meat!', 'Baker! Hell Yeah!', 'Baker has class!', 'Baker comes first in your face!', 'Baker Women Soft Skin!', 'Baker Comes Early!', 'Baker! Hell No!', 'Baker Women Look like Men'],
'hanszen': ['Hanszen’s got the gonorrhea … oooh-ahhh', 'Hanszen Rocks My Face Off', 'Hanszen’s got that ramma-jamma… oooh-ahhh', 'Harry Fucking Hanszen - Hanszen, Hanszen, Yeah!', 'We Jack Off & We’re Nazis', 'Hanszen stole my high school cheer… oooh-ahhh',
'What time is it? Hanszen still sucks!', 'Hanszen’s got the gonorrhea … oooh-ahhh', 'Give me an S, Give me a T, Give me a D, now give it to Hanszen', '(Harry Fucking Hanszen) SUCKS!'],
'weiss': ['Leave… Rice','Team Wiess', 'Pubic… Lice', 'Fist… Wiess', 'Tea-Bag… Wiess', 'Leave… Rice'],
'jones': ['Jones Wins Again!', 'JIBA','Knock Knock! Whose there? Jones. Jones who? Jones Bitch!', 'Hooray for Jones! HUZZAH!', 'You! F*ck You! - Jones? F*ck Jones!', 'Jones is statistically the worst college!', 'Jones Blows Goats!', 'Brown is Jones, Jones is Brown, Brown is Sh*t, Sh*t is Jones', 'Mary Gibbs Jones [is our bitch (swatting)]' ,'Jones says, watch us pee! We say no, no means no, Jones, no means no','Fortune and glory, kid. Fortune and glory'],
'brown': ['Brown is sh*t, sh*t is brown', 'Brown Shit We’re Bad', 'Longer Stronger Deeper Brown', 'Brown is sweet, we’re nice people', 'Bow down to Brown (x3)', 'F*ck You! We’re from Brown, Bitch!', 'Brown is Shit, Shit is Brown', 'Brown is undeniably the worst college', 'Brown is Jones, Jones is Brown' ],
'lovett': ['Toa~ster', 'Toaster! Toaster!!', 'Lovett Hate It Burn It Down!', 'Lovett Hate It Burn It Down!', 'Do Good, Do Right. Wash behind your ears. Don’t drink, don’t smoke. And respect your peers. We are the best college, all the others cuss. Edgar Odell Lovett, yay for us!'],
'sid': ['Sid Rich, you’re so tall, something else must be small', 'Sid Rich! Sid Rich Rules! Death From Above!', 'Sid is king, toil in our salt mines', 'Bow Down B**ch, We’re Sid Rich', 'Sid is Huge! Suck Our C**k!', 'Sid Rich! Sid Rich blows! Death From Behind!'],
'will_rice': [ 'Will Rice Will Cheat', 'Will Rice Will Sweep', 'O-Week, Beer Bike, & The Rest. We know Will Rice is the Best. Do we have to say it twice? Hell No! Go Will Rice!', 'F*CK WILL RICE'],
'martel': ['Martel is not a college', 'Martel, What is your profession? HUAH HUAH HUAH!', 'Social Rejects', 'Martel is not a sh*t hole'],
'mcmurtry': ['McDuncan','McMutry is in tents!', 'Buh duh duh duh duh… Suck it!', 'Where’s your commons? (claps)', 'McMurtry?! Meh…', 'McMurtry! What? McMurtry! F*ck Yeah!'],
'duncan':['McDuncan', 'Dunc is Crunk!', 'Burn the forest! Buy a hummer! Punt a panda! F*ck Duncan!', 'DUN-CAN’T!'],
'owl-dy': ['Owl-dy, how can I help you?', 'Owl-dy, have you found the Easter Egg yet?', 'Owl-dy, is that how you say Howdy?']
}



class resource:
''''
declare resource class for campus resource. takes in 4 inpus: name of the resource, web-address, phone number, the action
this class comes with getter function for returning these stored values.
''''
	def __init__(self, name, url, number, available_web_action):
		self.name = name
		self.url = url
		self.number = number
		self.action = available_web_action

	def get_name(self):
		return self.name

	def get_url(self):
		return self.url

	def get_num(self):
		return self.number

	def get_action(self):
		return self.action

# declare campus rescoures
rupd = resource('RUPD', 'https://rupd.rice.edu/', '+17133486000', 'Visit RUPD Website')
fondren = resource('Fondren', 'https://rooms.library.rice.edu/', '+17133485698', 'Reserve Fondy')
h_and_d = resource('H & D', 'http://dining.rice.edu/', '+1713348-5445', 'Check Menu')
registrar = resource('Registrar', 'https://esther.rice.edu', '+17133484999', 'Check Esther')
ccd = resource('CCD', 'https://rice.joinhandshake.com/', '+17133484055', 'Check Handshake')
health_service = resource("Health Service", 'https://health.rice.edu/', '+17133484966', 'Health Service Web')
bus = resource('Campus Bus Ride', 'http://www.rice.ridesystems.net/', '+17133485223', 'Bus Map')

#mapping requested resource to the resource object
directory = {'fondren' : fondren,'h&d': h_and_d, 'health_service' : health_service,
'rupd': rupd, 'registrar':registrar, 'ccd': ccd}

easter_egg_info = {
'Fortune' : 'Congratulations, you have found the Easter Egg (the Fortune, the treasure?)!!      “…Indiana Jones. I always knew someday you’d come walking back through my door. I never doubted that. Something made it inevitable.”',
'easter_egg': 'If you are looking for the Easter Egg. The key is hidden inside one of the college cheers. You need to find the key, and reply it to me. Good luck!'
}

#mapping a situation to the approiate campus resrouce
situation = {'lib_room': fondren,
'food': h_and_d,
'help': rupd,
'sick': health_service,
'bus': bus}

#packing the return into buttons for the facebook template API
def call_button(service):
	title = 'Call' + " " + service.get_name()
	return {"type":"phone_number","title":title,"payload":service.get_num()}

def url_button(service):
	title = service.get_action()
	return {"type": "web_url","url": service.get_url(),"title": title,}


access_token = "WG4AP4DW6BTREON25CTCTHRTPD2LI6WC"

client = Wit(access_token = access_token)

###########################################################



# For testing locally
message_text = 'h and d'

def wit_response(message_text):
	'''
	Input is user text message. call NLP to understand the message, 
	then return a break_down of the entities in the message. 
	'''

	#received the message after being processed by NLP
	received = client.message(message_text)
	print (received)
	
	entities = list(received['entities'])

	action = None
	service = None
	college = None
	greeting = None
	situation = None
	thank = None
	bye = None

    # Breaking down received messages to entities
	for entity in entities:
		if entity == 'intent' and received['entities'][entity][0]['confidence'] > 0.7:
			action = received['entities'][entity][0]['value']
		if entity == 'service' and received['entities'][entity][0]['confidence'] > 0.65:
			service = received['entities'][entity][0]['value']
		if entity == 'residential_college'and received['entities'][entity][0]['confidence'] > 0.65:
			college = received['entities'][entity][0]['value']
		if entity == 'greetings'and received['entities'][entity][0]['confidence'] > 0.8:
			greeting = received['entities'][entity][0]['value']
		if entity == 'situation'and received['entities'][entity][0]['confidence'] > 0.65:
			situation = received['entities'][entity][0]['value']
		if entity == 'thanks'and received['entities'][entity][0]['confidence'] > 0.8:
			thank = received['entities'][entity][0]['value']
		if entity == 'bye'and received['entities'][entity][0]['confidence'] > 0.8:
			bye = received['entities'][entity][0]['value']
			

	break_down = {'college':college, 'action':action, 'service': service, 'greetings': greeting, 'situation': situation, 'thanks': thank, 'bye': bye}

	return break_down

def talk_back(break_down):
	'''
	this function decides how to respond to the user based on the break_down
	'''

    # provide services according to intent
	if break_down['action'] != None:
        
        #return a phone number based on the service if available
		if break_down['action']  == 'call':
			if break_down['service'] != None and break_down['service'] in directory:
				#make a call button to be returned
				element = [call_button(directory[break_down['service']])]
			else:
				element = 'Service not available'
			return element

		#return a link to room reservation at the library
		if break_down['action'] == 'reserve':
			return [url_button(fondren)]

		#easter egg
		if break_down['action'] == 'Fortune':
			return easter_egg_info['Fortune']
		if break_down['action'] == 'easter_egg':
			return easter_egg_info['easter_egg']

	# return the useful info when in a special situation
	if break_down['situation'] != None and break_down['situation'] in situation:
		resource = situation[break_down['situation']] 
		url = url_button(resource)
		call = call_button(resource)
		return [url, call]
    
    # return related infomation when asked for a service
	if break_down['service'] != None and break_down['service'] in directory:
		resource = directory[break_down['service']]
		url = url_button(resource)
		call = call_button(resource)
		# return two bottons, one for a web action, one for dialing
		return [url, call]

	# reurn a college cheer
	if break_down['college'] != None and break_down['college'] in cheer:
		return random.choice(cheer[break_down['college']])
		#return cheer[break_down['college']][0]

	# retrun a greeting if was greeted
	if break_down['greetings'] == 'true':
		return 'Owl-dy, how can I help you? [try to tell me about your college?]'

	# retrun a you're welcome if was thanks
	if break_down['thanks'] == 'true':
		return 'Owl-dy, no problem. Happy to help :)'

	# retrun a you're welcome if was thanks
	if break_down['bye'] == 'true':
		return 'See you, hope you have a R-owl-dy day! Talk to me to find out more about the Easter Egg next time :)'

    # if don't understand sender's message, return i dont understand
	else:
		return 'Your Wisdom Is Unconventional. I have trouble understanding :('

counter = 0
while counter <= 2 :
	break_down = wit_response(message_text)
	print (break_down)
	print (talk_back(break_down))
	counter += 1




