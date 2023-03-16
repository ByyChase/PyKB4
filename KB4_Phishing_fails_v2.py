import requests, csv



URL = 'https://us.api.knowbe4.com/v1/phishing/campaigns'
api_key = 'replace with API key'
psts_Numbers = []
campaign_names = []
dates = []
Temp_Campaign_Data = []
Total_Campaign_Data = []
pagenumber = 1

#Calling the API
numpages = requests.get(URL, headers = { 'Authorization': 'Bearer ' + api_key}, params = {'page': 1}).json()



for x in numpages:
    psts = x.get('psts')
    create_date = str(x.get('create_date'))
    create_date = (create_date.split('T'))[0]
    name = str(x.get('name'))

    for sx in psts:
        pst_id = str(sx.get('pst_id'))
        psts_Numbers.append(pst_id)  
        dates.append(create_date)
        campaign_names.append(name)


for y in range(len(psts_Numbers)):

    try:
        campaign_temp = requests.get('https://us.api.knowbe4.com/v1/phishing/security_tests/' + psts_Numbers[y] +  '/recipients', headers = { 'Authorization': 'Bearer ' + api_key}, params = {'page': pagenumber}).json()
        campaign = campaign_temp
    except:
        pass

    while campaign_temp:
        campaign += campaign_temp
        
        try:
            campaign_temp = requests.get('https://us.api.knowbe4.com/v1/phishing/security_tests/' + psts_Numbers[y] +  '/recipients', headers = { 'Authorization': 'Bearer ' + api_key}, params = {'page': pagenumber}).json()

        except:
            pass

        pagenumber += 1 


   
    for data in campaign:

        recipient_id = str(data.get('recipient_id'))
        pst_id_email = str(data.get('pst_id'))
        user_id = str((data.get('user')).get('id'))
        first_name = str((data.get('user')).get('first_name'))
        last_name = str((data.get('user')).get('last_name'))
        email = str((data.get('user')).get('email'))
        template_id = str((data.get('template')).get('id'))
        template_name = str((data.get('template')).get('name'))
        scheduled_at = str(data.get('scheduled_at'))
        delivered_at = str(data.get('delivered_at'))
        opened_at = str(data.get('opened_at'))
        clicked_at = str(data.get('clicked_at'))
        replied_at = str(data.get('replied_at'))
        attachment_opened_at = str(data.get('attachment_opened_at'))
        macro_enabled_at = str(data.get('macro_enabled_at'))
        data_entered_at = str(data.get('data_entered_at'))
        vulnerable_plugins_at = str(data.get('vulnerable_plugins_at'))
        exploited_at = str(data.get('exploited_at'))
        reported_at = str(data.get('reported_at'))
        bounced_at = str(data.get('bounced_at'))
        ip = str(data.get('ip'))
        ip_location = str(data.get('ip_location'))
        browser = str(data.get('browser'))
        browser_version = str(data.get('browser_version'))
        os = str(data.get('os'))

        Temp_Campaign_Data = [recipient_id, pst_id_email, user_id, first_name, last_name, email, template_id, template_name, scheduled_at, delivered_at, opened_at, clicked_at, replied_at, attachment_opened_at, macro_enabled_at, data_entered_at, vulnerable_plugins_at, exploited_at, reported_at, bounced_at, ip, ip_location, browser, browser_version, os]
        Total_Campaign_Data.append(Temp_Campaign_Data)
    
    if y != (len(psts_Numbers) - 1):
        if  campaign_names[y] !=campaign_names[y+1]:
            count = 0

            filename = campaign_names[y] + '_' + dates[y] + '.csv'

            filename = filename.replace(':', '_')
            filename = filename.replace(' ', '_')

            with open('C:/' + filename, mode='w', newline='', encoding="utf-8") as Phishing_File:
                Phishing_Writer = csv.writer(Phishing_File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                print('\n\nMaking file ' + campaign_names[y] + '_' + dates[y] + '.csv')
                Phishing_Writer.writerow(['Recipient ID', 'PST ID', 'User ID', 'First Name', 'Last Name', 'Email', 'Template ID', 'Template Name', 'Scheduled At', 'Delivered At', 'Opened At', 'Clicked At', 'Replied At', 'Attachment Opened At', 'Macro Enabled At', 'Data Entered At','Vulnerable Plugin At', 'Exploited At', 'Reported At', 'Bounced At', 'IP', 'IP Location', 'Browser', 'Browser Version', 'OS'])
                print('rows created\n')
                for k in Total_Campaign_Data:
                    Phishing_Writer.writerow([k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8], k[9], k[10], k[11], k[12], k[13], k[14], k[15], k[16], k[18], k[19], k[20], k[21], k[22], k[23]])
                    count = count + 1

            Phishing_File.close()
            Total_Campaign_Data = []
            
            

    pagenumber = 0
    print("rows printed: " + str(count))

filename = campaign_names[y] + '_' + dates[y] + '.csv'

filename = filename.replace(':', '_')
filename = filename.replace(' ', '_')

with open('C:/' + filename, mode='w', newline='', encoding="utf-8") as Phishing_File:
    Phishing_Writer = csv.writer(Phishing_File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    Phishing_Writer.writerow(['Recipient ID', 'PST ID', 'User ID', 'First Name', 'Last Name', 'Email', 'Template ID', 'Template Name', 'Scheduled At', 'Delivered At', 'Opened At', 'Clicked At', 'Replied At', 'Attachment Opened At', 'Macro Enabled At', 'Data Entered At', 'Vulnerable Plugin At', 'Exploited At', 'Reported At', 'Bounced At', 'IP', 'IP Location', 'Browser', 'Browser Version', 'OS'])

    for k in Total_Campaign_Data:
        Phishing_Writer.writerow([k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8], k[9], k[10], k[11], k[12], k[13], k[14], k[15], k[16], k[18], k[19], k[20], k[21], k[22], k[23]])

Phishing_File.close()