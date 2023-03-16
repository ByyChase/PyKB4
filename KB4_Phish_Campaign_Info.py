import requests, csv


#Initializing Variables
URL = 'https://us.api.knowbe4.com/v1/phishing/campaigns'
api_key = 'replace with API key'
pagenum = 1
numpages = requests.get(URL, headers = { 'Authorization': 'Bearer ' + api_key}).json()
Groups_in_Campaign = ""
Group = []
Campaign_Info = []
Campaign = []

#Looping through the API results and placing each camapign into a list
for x in numpages:
    campaign_id = str(x.get('campaign_id'))
    name = str(x.get('name'))
    last_phish_prone_percentage = str(x.get('last_phish_prone_percentage'))
    last_run = str(x.get('last_run'))
    status = str(x.get('status'))
    hidden = str(x.get('hidden'))
    send_duration = str(x.get('send_duration'))
    track_duration = str(x.get('track_duration'))
    frequency = str(x.get('frequency'))
    create_date = str(x.get('create_date'))
    psts_count = str(x.get('psts_count'))
    groups = x.get('groups')

    print(groups)

    for xx in groups:
        group_id = str(xx.get('group_id'))
        group_name = str(xx.get('name'))

        Groups_in_Campaign = group_id + ", " + group_name
        Group.append(Groups_in_Campaign)

    while len(Group) < 14:
        Group.append('N/A')


    Campaign_Info = [campaign_id, name, last_phish_prone_percentage, last_run, status, hidden, send_duration, track_duration, frequency, create_date, psts_count, Group]
    Campaign.append(Campaign_Info)
    Group = []


        

#Opening a file to export the campaign information 
with open('KB4Campaigns.csv', mode='w', newline='', encoding="utf-8") as Campaign_info:
    Campaign_writer = csv.writer(Campaign_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    Campaign_writer.writerow(['Campaign ID', 'Name', 'Last Phish Prone Percentage', 'Last Run', 'Status', 'Hidden', 'Send Duration', 'Track Duration', 'Frequency', 'Create Date', 'PSTS Count', 'Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6', 'Group 7', 'Group 8', 'Group 9', 'Group 10','Group 11','Group 12','Group 13','Group 14'])

    for x in Campaign:
        Campaign_writer.writerow([x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11][0], x[11][1], x[11][2], x[11][3], x[11][4], x[11][5], x[11][6], x[11][7], x[11][8], x[11][9], x[11][10], x[11][11], x[11][12], x[11][13]])

Campaign_info.close()