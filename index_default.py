import requests
from typing import Dict, Optional, List

class WhatsAppTemplateSender:
    def __init__(self, phone_number_id: str, access_token: str, api_version: str = "v22.0"):
        """
        Initialize WhatsApp Template Sender
        
        Args:
            phone_number_id: Your WhatsApp Business Account Phone Number ID
            access_token: Your WhatsApp Cloud API access token
            api_version: Facebook Graph API version (default: v21.0)
        """
        self.base_url = f"https://graph.facebook.com/{api_version}/{phone_number_id}/messages"
        # Make sure the phone number ID is correct and doesn't have any extra spaces
        if not phone_number_id.isdigit():
            raise ValueError("Phone number ID should contain only digits")
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def send_template(
        self,
        to: str,
        template_name: str,
        language_code: str = "en",
        components: Optional[List[Dict]] = None
    ) -> Dict:
        """
        Send a WhatsApp template message
        
        Args:
            to: Recipient's phone number with country code (without '+')
            template_name: Name of the approved template
            language_code: Language code (default: "en" for English)
            components: Optional template components (buttons, parameters, etc.)
            
        Returns:
            API response as a dictionary
        """
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }
        
        if components:
            payload["template"]["components"] = components
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "status_code": getattr(e.response, 'status_code', None),
                "response": e.response.json() if e.response else None
            }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your credentials
        phone_number_id = "779202445285394"  # Make sure this is your correct phone number ID
        access_token = "EAALMPC0iJqEBPymSSZBQWmGaru10YvV9DH7wjKxEaSbh7Fwpkm9OtxiBaFv0k7RX7DXF5MVPSQxJOWxQlVJhPpHOItlZBBAIlQPgBjJmCU7KbKTWVsi7ile49PC2yOn3QXF0oZC25pvejaYH3h9XVGmLuHYei7CfiPUbvqSbLnnVoKswZBBchUEafHs6pKSR4EpeNJEZBPdo8Ll2875JlqmYvwYlhhJFjcB0gspZAdB8cv6r0DPzzkYe4O8ZANKG1EMkIe3SQMr0ekFZAqLxvqpp9QZDZD"
        
        print(f"Attempting to send message with Phone Number ID: {phone_number_id}")
        
        whatsapp = WhatsAppTemplateSender(
            phone_number_id=phone_number_id,
            access_token=access_token
        )
        
        # Send the template message
        print("Sending template message...")
        # Example with template parameters
        response = whatsapp.send_template(
            to="917319740112",  # Recipient's phone number with country code (without '+')
            template_name="sankhya_greetin",  # Your custom template name
            language_code="en_US",  # Language code for the template
            components=[
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": "Customer Name"}  # This will replace {{1}} in your template
                    ]
                }
            ]
        )
        
        print("\n--- Template Message Response ---")
        if 'error' in response:
            print(f"❌ Error: {response['error']}")
            if 'response' in response and response['response']:
                print(f"API Response: {response['response']}")
        else:
            print("✅ Message sent successfully!")
            if 'messages' in response:
                print(f"Message ID: {response['messages'][0]['id']}")
        
        print("\nFull Response:", response)
        
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        if hasattr(e, 'response') and e.response:
            print(f"Response status: {e.response.status_code}")
            try:
                print(f"Response content: {e.response.json()}")
            except:
                print(f"Response text: {e.response.text}")