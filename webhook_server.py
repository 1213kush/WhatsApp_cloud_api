from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ngrok config add-authtoken 2srHFnhm1AjFEruWzLrak7Hzi7a_SBwWN77vuMYS4qmePmRM"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("✅ WEBHOOK VERIFIED!")
            return challenge, 200
        else:
            print("❌ VERIFICATION FAILED.")
            return "Verification failed", 403

    elif request.method == "POST":
        data = request.get_json()
        print("📩 Received:", data)
        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(port=8000)
