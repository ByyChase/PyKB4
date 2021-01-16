import requests 

class KnowBe4:
    def __init__(self, API_Key):
        self.api_key = api_key

    def account(self):
        jsondata = requests.get('https://us.api.knowbe4.com/v1/account', headers = {'Authorization': 'Bearer ' + self.api_key}).json
        return jsondata

    def users(self):
        page_number = 1
        cont = True
        return_data = []
        while cont:
            try:
                json_data = requests.get('https://us.api.knowbe4.com/v1/users', headers = {'Authorization': 'Bearer ' + self.api_key}, param = {'page' : page_number}).json
            
            except:
                cont = False
            return_data += json_data
            page_number += 1

        return return_data
