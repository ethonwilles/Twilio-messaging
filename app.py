from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import config
import pymongo
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['twilioDatabase']

mycol = mydb["users"]


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



# index page routes and logic
@app.route('/', methods=['GET'])
def render():
    return render_template('index.html')


# submission page routes and logic
@app.route('/submission.html', methods=['GET'])
def render_sub():
    
    return render_template('submission.html')
    message = request.form['message']
    print(message)

# Conversation page routes and logic
@app.route('/conversations.html', methods=["GET"])
def render_conv():
    return render_template('conversations.html')


# Sign up Page routes and logic
@app.route('/signup.html', methods=["GET"])
def render_signup():
    return render_template('signup.html')

@app.route('/signup.html', methods=['POST'])
def add_to_database():

    new_dict = {'username': f'{request.form["username"]}', 'password' : f'{request.form["password"]}'}
    mycol.insert_one(new_dict)
    print(mycol.find_one())
    return render_template('/conversations.html')


# send sms?
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








if __name__ == '__main__':
    app.run(port=80,debug=True)


print(mycol.fine_one())