import requests

class KnowBe4:
    def __init__(self, api_key):
        self.api_key = api_key
          
    def build_non_page_url(api_key, url):
        jsondata = requests.get(url, headers = {'Authorization': 'Bearer ' + self.api_key}).json
        return jsondata
    
    def build_page_url(api_key, url):
        page_number = 1
        cont = True
        return_data = []
        while cont:
            try:
                json_data = requests.get(url, headers = {'Authorization': 'Bearer ' + api_key}, param = {'page' : page_number}).json
            
            except:
                cont = False
            return_data += json_data
            page_number += 1
        
    def account(self):
        url = 'https://us.api.knowbe4.com/v1/account'
        return build_non_page_url(self.api_key, url)

    def users(self):
        url = 'https://us.api.knowbe4.com/v1/users'
        return build_page_url(self.api_key, url)
            
    def users_in_group(self, group_id):
        url = 'https://us.api.knowbe4.com/v1/groups/' + group_id + '/members'
        return build_non_page_url(self.api_key, url)
    
    def user(self, user_id):
        url = 'https://us.api.knowbe4.com/v1/users/' + user_id + ''
        return build_page_url(self.api_key, url)

    def groups(self):
        url = 'https://us.api.knowbe4.com/v1/groups'
        return build_non_page_url(self.api_key, url)
               
    def user(self, group_id):
        url = 'https://us.api.knowbe4.com/v1/groups/' + group_id + ''
        return build_non_page_url(self.api_key, url)

    def groups(self):
        url = 'https://us.api.knowbe4.com/v1/groups'
        return build_non_page_url(self.api_key, url)
    
    def all_phishing_capaigns(self):
        url = 'https://eu.api.knowbe4.com/v1/phishing/campaigns'
        return build_non_page_url(self.api_key, url)
    
    def phishing_campaign(self, campaign_id):
        url = 'https://us.api.knowbe4.com/v1/phishing/campaigns/' + campaign_id + ''
        return build_non_page_url(self.api_key, url)
    
    def all_phishing_security_tests(self):
        url = 'https://us.api.knowbe4.com/v1/phishing/security_tests'  
        return build_non_page_url(self.api_key, url)  
    
    def all_phishing_security_test_from_campaign(self, campaign_id):
        url = 'https://us.api.knowbe4.com/v1/phishing/campaigns/' + campaign_id + '/security_tests'
        return build_non_page_url(self.api_key, url)  
    
    def phishing_security_test(self, pst_id):
        url = 'https://us.api.knowbe4.com/v1/phishing/security_tests/' + pst_id + ''
        return build_non_page_url(self.api_key, url) 
        
    def security_test_results(self, pst_id):
        url = 'https://us.api.knowbe4.com/v1/phishing/security_tests/' + pst_id + '/recipients'
        return build_non_page_url(self.api_key, url) 
    
    def user_security_test_results(self, pst_id, recipient_id):
        url = 'https://us.api.knowbe4.com/v1/phishing/security_tests/' + pst_id + '/recipients/' + recipient_id + ''
        return build_non_page_url(self.api_key, url) 