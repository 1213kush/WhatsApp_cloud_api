from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Set port and verify_token from environment variables
PORT = int(os.environ.get('PORT', 3000))
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')

# Route for GET requests (webhook verification)
@app.route('/', methods=['GET'])
def verify_webhook():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        print('WEBHOOK VERIFIED')
        return challenge, 200
    else:
        return 'Verification token mismatch', 403

# Route for POST requests (webhook events)
@app.route('/', methods=['POST'])
def webhook():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'\n\nWebhook received {timestamp}\n')
    print(request.json)
    return '', 200

if __name__ == '__main__':
    print(f'\nListening on port {PORT}\n')
    app.run(host='0.0.0.0', port=PORT)
