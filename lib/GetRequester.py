import requests


class GetRequester:
    """
    A class for retrieving data from a remote API endpoint.
    """

    def __init__(self, endpoint):
        """
        Initialize the GetRequester with an endpoint URL.
        """
        self.endpoint = endpoint

    def get_response_body(self):
        """
        Send a GET request and return the raw response body as bytes.
        """
        response = requests.get(self.endpoint)
        return response.content

    def load_json(self):
        """
        Send a GET request and return the response converted to Python data.
        """
        response = requests.get(self.endpoint)
        return response.json()