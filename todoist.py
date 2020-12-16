import json
from typing import Any, Union

import oauth2

class TodoIst:
    def __init__(self, filename):
        self.filename = filename
        self.client = oauth2.oauth()
        self.client.authorize()
        # self.client.new_tokens()

    def test_api(self):
        print('Authenticating...')
        print(self.client.auth_header())


