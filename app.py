from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import config
from flask_pymongo import PyMongo
app = Flask(__name__)

account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_TOKEN

client = Client(account_sid,auth_token)

contacts = {
    'Tyler': '8017352899',
    'Terra': '8018647444',
    'Alicia': ''
}

list_of_contacts = []
for contact in contacts:
    list_of_contacts.append(contact)
print(list_of_contacts)

@app.route('/', methods=['GET'])
def render():
    return render_template('index.html')

@app.route('/submission.html', methods=['GET'])
def render_sub():
    
    return render_template('submission.html')
    message = request.form['message']
    print(message)

@app.route('/send_sms', methods=['VIEW'])
def send_sms():
    message = client.messages \
                    .create(
                    to=('+1' + contacts[str(input('who would you like to send the message to?: '))].capitalize()),
                    from_='+18016163624',
                    body=(input('What would you like your message to say?: ')))

@app.route("/sms", methods=['POST'])
def sms_response():

    
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()

    print(message_body)
    resp.message(input('What would you like to say back?: '))
    return str(resp)


# Mongo DB
app.config['MONGO_URI'] = "mongodb://localhost:27017/twilioDatabase"
mongo = PyMongo(app)




if __name__ == '__main__':
    app.run(port=80,debug=True)