import requests, csv

#Initializing Variables
return_data = ""
group_data = []
url = 'https://us.api.knowbe4.com/v1/groups'
api_key = 'replace with API key'

#Calling the KB4 API
json_data = requests.get(url, headers = {'Authorization': 'Bearer ' + api_key}).json()

#Looping through the data from the API response          
for x in json_data:
    name = str(x.get('name'))
    group_id = str(x.get('id'))
    group_type = str(x.get('group_type'))
    adi_guid = str(x.get('adi_guid'))
    member_count = str(x.get('member_count'))
    current_risk_score = str(x.get('current_risk_score'))
    status = str(x.get('status'))

    temp_group_data = [name, group_id, group_type, adi_guid, member_count, current_risk_score, status]
    group_data.append(temp_group_data)

#Exporting the API data into a CSV
with open('KB4Groups.csv', mode='w', newline='', encoding="utf-8") as Group_Info:
    Group_writer = csv.writer(Group_Info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    Group_writer.writerow(['Name', 'Group ID', 'Group Type', 'ADI GUID', 'Member Count', 'Current Risk Score', 'Status'])

    for x in group_data:
        Group_writer.writerow([x[0], x[1], x[2], x[3], x[4], x[5], x[6]])

Group_Info.close()