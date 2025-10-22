import requests
import json


# WhatsApp Cloud API URL
url = "https://graph.facebook.com/v21.0/779202445285394/messages"

# Replace this with your valid access token
access_token = "EAALMPC0iJqEBPymSSZBQWmGaru10YvV9DH7wjKxEaSbh7Fwpkm9OtxiBaFv0k7RX7DXF5MVPSQxJOWxQlVJhPpHOItlZBBAIlQPgBjJmCU7KbKTWVsi7ile49PC2yOn3QXF0oZC25pvejaYH3h9XVGmLuHYei7CfiPUbvqSbLnnVoKswZBBchUEafHs6pKSR4EpeNJEZBPdo8Ll2875JlqmYvwYlhhJFjcB0gspZAdB8cv6r0DPzzkYe4O8ZANKG1EMkIe3SQMr0ekFZAqLxvqpp9QZDZD"

# Set headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Message payload
payload = {
    "messaging_product": "whatsapp",
    "to": "917319740112",  # Replace with your receiver's phone number (with country code, no +)
    "type": "text",
    "text": {
        "preview_url": False,
        "body": "Hare Krishna 🙏✨\nThis is a test message from Sankhya Systems Pvt. Ltd. using WhatsApp Cloud API!"
    }
}

# Send POST request
print("\nSending message...")
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    response_data = response.json()
    
    print("\n--- Message Response ---")
    if 'messages' in response_data and response_data['messages']:
        message_info = response_data['messages'][0]
        print(f"✅ Message ID: {message_info.get('id', 'N/A')}")
        if 'message_status' in message_info:
            print(f"Status: {message_info['message_status'].upper()}")
        else:
            print("Status: SENT (awaiting status update)")
    else:
        print("✅ Message sent successfully!")
    
    print("\n--- Full Response ---")
    print(json.dumps(response_data, indent=2))
    
except requests.exceptions.RequestException as e:
    print("\n--- Message Sending Failed ---")
    print(f"❌ Error: {str(e)}")
    if hasattr(e, 'response') and e.response:
        print(f"Status Code: {e.response.status_code}")
        try:
            error_data = e.response.json()
            print("Error Details:", error_data)
        except:
            print("Response:", e.response.text)
