from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

# Initialize Flask app
app = Flask(__name__)

# Twilio Account Details
ACCOUNT_SID = "your_account_sid"  # Replace with your Twilio Account SID
AUTH_TOKEN = "your_auth_token"    # Replace with your Twilio Auth Token
TWILIO_NUMBER = "your_twilio_phone_number"  # Replace with your Twilio phone number
VICTIM_NUMBER = "victim_phone_number"  # Replace with the victim's phone number (for testing)

# Route for the simulated vishing call
@app.route("/vishing", methods=["POST"])
def vishing_call():
    response = VoiceResponse()
    response.say("Hello, this is a call from your bank.")
    response.say("We noticed suspicious activity on your debit card ending in 1234.")
    response.say("For security verification, please provide the one-time password sent to your phone.")
    response.pause(length=3)
    response.say("Please note: Failure to provide the OTP will result in the temporary suspension of your card.")
    return str(response)

# Function to initiate the call
def initiate_call():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(
        url="https://4814-173-54-161-220.ngrok-free.app/vishing",  # Replace with your ngrok URL
        to=VICTIM_NUMBER,
        from_=TWILIO_NUMBER
    )
    print(f"Call initiated: {call.sid}")

if __name__ == "__main__":
    print("Starting Flask server...")
    print("Call http://localhost:8000/initiate_call to start the simulation")
    app.run(port=8000)

