from os import environ as env

import globals

import sift


class VerificationAPI:
    # Get the value of API_KEY from environment variable
    api_key = env["API_KEY"]
    client = sift.Client(api_key=api_key)
    globals.initialize()
    user_id = globals.user_id
    user_email = globals.user_email

    def send(self) -> sift.client.Response:
        properties = {
            "$user_id": self.user_id,
            "$send_to": self.user_email,
            "$verification_type": "$email",
            "$brand_name": "MyTopBrand",
            "$language": "en",
            "$site_country": "IN",
            "$event": {
                "$session_id": "SOME_SESSION_ID",
                "$verified_event": "$login",
                "$verified_entity_id": "SOME_SESSION_ID",
                "$reason": "$automated_rule",
                "$ip": "192.168.1.1",
                "$browser": {
                    "$user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                    "$accept_language": "en-US",
                    "$content_language": "en-GB",
                },
            },
        }
        return self.client.verification_send(properties)

    def resend(self) -> sift.client.Response:
        properties = {
            "$user_id": self.user_id,
            "$verified_event": "$login",
            "$verified_entity_id": "SOME_SESSION_ID",
        }
        return self.client.verification_resend(properties)

    def check(self) -> sift.client.Response:
        properties = {
            "$user_id": self.user_id,
            "$code": "123456",
            "$verified_event": "$login",
            "$verified_entity_id": "SOME_SESSION_ID",
        }
        return self.client.verification_check(properties)
