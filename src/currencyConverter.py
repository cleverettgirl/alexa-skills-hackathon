"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import urllib2 as urllib
import json


currencies = json.loads("{ \"UAE dirhams\": \"AED\",  \"Afghan afghanis\": \"AFN\",  \"Albanian leke\": \"ALL\",  \"Armenian dram\": \"AMD\",  \"Netherlands Antillean guilders\": \"ANG\",  \"Dutch Antillean guilders\": \"ANG\",  \"Netherlands guilders\": \"ANG\",  \"Dutch guilders\": \"ANG\",  \"Angolan kwanza\": \"AOA\",  \"Argentine pesos\": \"ARS\",  \"Australian dollars\": \"AUD\",  \"Aruban florin\": \"AWG\",  \"Azerbaijanian manat\": \"AZN\",  \"Bosnia and Herzegovina convertible marks\": \"BAM\",  \"Bosnia and Herzegovina marks\": \"BAM\",  \"Bosnia and Herzegovinan marks\": \"BAM\",  \"Barbadian dollars\": \"BBD\",  \"Bangladeshi taka\": \"BDT\",  \"Bangladeshian taka\": \"BDT\",  \"Bulgarian leva\": \"BGN\",  \"Bahraini dinara\": \"BHD\",  \"Bahrainian dinara\": \"BHD\",  \"Burundi francs\": \"BIF\",  \"Burundian francs\": \"BIF\",  \"Bermudian dollars\": \"BMD\",  \"Brunei dollars\": \"BND\",  \"Bolivian bolivianos\": \"BOB\",  \"Brasilien reais\": \"BRL\",  \"Brazilian reais\": \"BRL\",  \"Bahamian dollars\": \"BSD\",  \"Bitcoins\": \"BTC\",  \"Bhutanese ngultrum\": \"BTN\",  \"Botswanan pulas\": \"BWP\",  \"New Belarusian ruble\": \"BYN\",  \"Belarusian ruble\": \"BYR\",  \"Belize dollars\": \"BZD\",  \"Canadian dollars\": \"CAD\",  \"Congolese francs\": \"CDF\",  \"Swiss Francs\": \"CHF\",  \"Unidades de fomento\": \"CLF\",  \"Chilean pesos\": \"CLP\",  \"Chinese yuan\": \"CNY\",  \"Colombian pesos\": \"COP\",  \"Costa Rican colones\": \"CRC\",  \"Cuban pesos\": \"CUP\",  \"Cape Verdean escudos\": \"CVE\",  \"Czech korun\": \"CZK\",  \"Djiboutian francs\": \"DJF\",  \"Danish kroner\": \"DKK\",  \"Dominican pesos\": \"DOP\",  \"Algerian dinara\": \"DZD\",  \"Egyptian pounds\": \"EGP\",  \"Eritrean nakfa\": \"ERN\",  \"Ethiopian birr\": \"ETB\",  \"European Union euros\": \"EUR\",  \"Fijian dollars\": \"FJD\",  \"Falkland Islands pounds\": \"FKP\",  \"British pounds sterling\": \"GBP\",  \"Georgian lari\": \"GEL\",  \"Ghanian cedis\": \"GHS\",  \"Gibraltar pounds\": \"GIP\",  \"Gambian dalasi\": \"GMD\",  \"Guinean Francs\": \"GNF\",  \"Guatemalan quetzales\": \"GTQ\",  \"Guyanese dollars\": \"GYD\",  \"Hong Kong dollars\": \"HKD\",  \"Honduran lempiras\": \"HNL\",  \"Croatian kuna\": \"HRK\",  \"Haitian gourdes\": \"HTG\",  \"Hungarian forint\": \"HUF\",  \"Indonesia Rupiahs\": \"IDR\",  \"Israeli shekalim hadash\": \"ILS\",  \"Indian Rupeess\": \"INR\",  \"Iraqi dinara\": \"IQD\",  \"Iranian rials\": \"IRR\",  \"Icelandic Kronur\": \"ISK\",  \"Jamaican dollars\": \"JMD\",  \"Jordanian diO\": \"JOD\",  \"American dollar\": \"usd\",  \"English pound\": \"GBP\",    \"UAE\": \"AED\",  \"Afghanistan\": \"AFN\",  \"Albania\": \"ALL\",  \"Armenia\": \"AMD\",  \"Netherlands\": \"ANG\",  \"Angola\": \"AOA\",  \"Argentina\": \"ARS\",  \"Australia\": \"AUD\",  \"Aruba\": \"AWG\",  \"Azerbaijanian manat\": \"AZN\",  \"Bosnia and Herzegovina\": \"BAM\",  \"Barbados\": \"BBD\",  \"Bangladesh\": \"BDT\",  \"Bulgaria\": \"BGN\",  \"Bahrain\": \"BHD\",  \"Burundi\": \"BIF\",  \"Bermuda\": \"BMD\",  \"Brunei\": \"BND\",  \"Bolivia\": \"BOB\",  \"Brazil\": \"BRL\",  \"Bahamas\": \"BSD\",  \"Bitcoin\": \"BTC\",  \"Bhutan\": \"BTN\",  \"Botswana\": \"BWP\",  \"Belarus\": \"BYR\",  \"Belize\": \"BZD\",  \"Canada\": \"CAD\",  \"Congo\": \"CDF\",  \"Switzerland\": \"CHF\",  \"Unidades de fomento\": \"CLF\",  \"Chile\": \"CLP\",  \"China\": \"CNY\",  \"Colombia\": \"COP\",  \"Costa Rica\": \"CRC\",  \"Cuba\": \"CUP\",  \"Cape Verde\": \"CVE\",  \"Czech\": \"CZK\",  \"Czech Republic\": \"CZK\",  \"Djibouti\": \"DJF\",  \"Denmark\": \"DKK\",  \"Dominican Republic\": \"DOP\",  \"Algeria\": \"DZD\",  \"Egypt\": \"EGP\",  \"Eritrea\": \"ERN\",  \"Ethiopia\": \"ETB\",  \"European Union\": \"EUR\",  \"Fiji\": \"FJD\",  \"Falkland Islands\": \"FKP\",  \"Great Britain\": \"GBP\",  \"England\": \"GBP\",  \"Georgia\": \"GEL\",  \"Ghana\": \"GHS\",  \"Gibraltar\": \"GIP\",  \"Gambia\": \"GMD\",  \"Guinea\": \"GNF\",  \"Guatemala\": \"GTQ\",  \"Guyana\": \"GYD\",  \"Hong Kong\": \"HKD\",  \"Honduras\": \"HNL\",  \"Croatian\": \"HRK\",  \"Haiti\": \"HTG\",  \"Hungary\": \"HUF\",  \"Indonesia\": \"IDR\",  \"Israel\": \"ILS\",  \"India\": \"INR\",  \"Iraq\": \"IQD\",  \"Iran\": \"IRR\",  \"Iceland\": \"ISK\",  \"Jamaica\": \"JMD\",  \"Jordan\": \"JOD\",  \"Afghan\": \"AFN\",  \"Albanian\": \"ALL\",  \"Armenian\": \"AMD\",  \"Dutch\": \"ANG\",  \"Angolan\": \"AOA\",  \"Argentine\": \"ARS\",  \"Australian\": \"AUD\",  \"Aruban\": \"AWG\",  \"Azerbaijanian\": \"AZN\",  \"Bosnian\": \"BAM\",  \"Barbadian\": \"BBD\",  \"Bangladeshi\": \"BDT\",  \"Bangladeshian\": \"BDT\",  \"Bulgarian\": \"BGN\",  \"Bahraini\": \"BHD\",  \"Bahrainian\": \"BHD\",  \"Burundi\": \"BIF\",  \"Burundian\": \"BIF\",  \"Bermudian\": \"BMD\",  \"Brunei\": \"BND\",  \"Bolivian\": \"BOB\",  \"Brasilien\": \"BRL\",  \"Brazilian\": \"BRL\",  \"Bahamian\": \"BSD\",  \"Bitcoin\": \"BTC\",  \"Bhutanese\": \"BTN\",  \"Botswanan\": \"BWP\",  \"Belarusian\": \"BYN\",  \"Belize\": \"BZD\",  \"Canadian\": \"CAD\",  \"Congolese\": \"CDF\",  \"Swiss\": \"CHF\",  \"Unidades de fomento\": \"CLF\",  \"Chilean\": \"CLP\",  \"Chinese\": \"CNY\",  \"Colombian\": \"COP\",  \"Costa Rican\": \"CRC\",  \"Cuban\": \"CUP\",  \"Cape Verdean\": \"CVE\",  \"Czech\": \"CZK\",  \"Czech Republican\": \"CZK\",  \"Djiboutian\": \"DJF\",  \"Danish\": \"DKK\",  \"Dominican\": \"DOP\",  \"Algerian\": \"DZD\",  \"Egyptian\": \"EGP\",  \"Eritrean\": \"ERN\",  \"Ethiopian\": \"ETB\",  \"European Union\": \"EUR\",  \"Fijian\": \"FJD\",  \"Falkland Islands\": \"FKP\",  \"Falkland\": \"FKP\",  \"British\": \"GBP\",  \"Georgian\": \"GEL\",  \"Ghanian\": \"GHS\",  \"Gibraltar\": \"GIP\",  \"Gambian\": \"GMD\",  \"Guinean\": \"GNF\",  \"Guatemalan\": \"GTQ\",  \"Guyanese\": \"GYD\",  \"Honduran\": \"HNL\",  \"Croatian\": \"HRK\",  \"Haitian\": \"HTG\",  \"Hungarian\": \"HUF\",  \"Indonesian\": \"IDR\",  \"Israeli\": \"ILS\",  \"Indian\": \"INR\",  \"Iraqi\": \"IQD\",  \"Iranian\": \"IRR\",  \"Icelandic\": \"ISK\",  \"Jamaican\": \"JMD\",  \"Jordanian\": \"JOD\", \"United States Dollars\": \"usd\",  \"American\": \"usd\",  \"English\": \"GBP\"}".lower())

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Forex Exchange. Please tell me the currency you want to convert."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me the currency you want to convert."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Foreign Exchange. Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_result_attributes(converted_rate):
    return {"result": converted_rate}


def get_exchange_amount(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    amount = 0
    exchangeFrom = ""
    exchangeTo = ""
    if 'amount' in intent['slots']:
        amount = intent['slots']['amount']['value']

    if 'exchangeFrom' in intent['slots']:
        exchangeFrom = intent['slots']['exchangeFrom']['value']

    if 'exchangeTo' in intent['slots']:
            exchangeTo = intent['slots']['exchangeTo']['value']

    if not amount and exchangeFrom and exchangeTo:
        speech_output = "I'm not sure what currency you want to convert. " \
                        "You can tell me something like convert 100 united states dollars to european union euros. " \
                        "Please try again."
        reprompt_text = "I'm not sure what currency you want to convert. " \
                        "You can tell me something like convert 100 united states dollars to european union euros. "
    else :
        print(amount)
        print(currencies[exchangeFrom.lower()])
        print(currencies[exchangeTo.lower()])

        response = urllib.urlopen("http://globalcurrencies.xignite.com/xGlobalCurrencies.json/ConvertRealTimeValue?_token=9176EFC7485E4DCBA6268392BEAED94F&From=" + currencies[exchangeFrom.lower()] + "&To="+ currencies[exchangeTo.lower()] +"&Amount=" + amount)

        if (response.getcode() == 200):
            html = response.read()
            # print(html)

            res = json.loads(html)
            # print(res)

            result = res['Result']


            session_attributes = create_result_attributes(res['Result'])
            speech_output = amount + " " + exchangeFrom + " is " + str(result) + " " + exchangeTo
            reprompt_text = "Please tell me the currency you want to convert."
        else:
            speech_output = "I'm not sure what currency you want to convert. " \
                            "Please try again."
            reprompt_text = "I'm not sure what currency you want to convert. " \
                            "You can tell me something like convert 100 united states dollars to european union euros. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# def get_color_from_session(intent, session):
#     session_attributes = {}
#     reprompt_text = None
#
#     if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
#         favorite_color = session['attributes']['favoriteColor']
#         speech_output = "Your favorite color is " + favorite_color + \
#                         ". Goodbye."
#         should_end_session = True
#     else:
#         speech_output = "I'm not sure what your favorite color is. " \
#                         "You can say, my favorite color is red."
#         should_end_session = False
#
#     # Setting reprompt_text to None signifies that we do not want to reprompt
#     # the user. If the user does not respond or says something that is not
#     # understood, the session will end.
#     return build_response(session_attributes, build_speechlet_response(
#         intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetExchangeRate":
        return get_exchange_amount(intent, session)
    # elif intent_name == "WhatsMyColorIntent":
    #     return get_color_from_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
