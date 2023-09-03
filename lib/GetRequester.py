import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response= requests.get(self.url)

        return response.content

    def load_json(self):

        response_body = self.get_response_body()
        response_text = response_body.decode('utf-8')  # Decode the bytes to a UTF-8 string
        URL_data = json.loads(response_text)  # Parse JSON data from the response text
        return URL_data
    
