import requests, csv, os

URL = 'https://us.api.knowbe4.com/v1/users'
api_key = 'replace with API key'
Userinfo = []
Users = []
pagenum = 0
numpages = 2
while numpages:
    pagenum = pagenum + 1
    numpages = requests.get(URL, headers = { 'Authorization': 'Bearer ' + api_key}, params = {'page': pagenum}).json()
    
    for x in numpages:
        user_id = str(x.get('id'))
        employee_number = str(x.get('employee_number'))
        first_name = str(x.get('first_name'))
        last_name = str(x.get('last_name'))
        job_title = str(x.get('job_title'))
        email = str(x.get('email'))
        phish_prone_percentage = str(x.get('phish_prone_percentage'))
        phone_number = str(x.get('phone_number'))
        extension = str(x.get('extension'))
        mobile_phone_number = str(x.get('mobile_phone_number'))
        location = str(x.get('location'))
        division = str(x.get('division'))
        manager_name = str(x.get('manager_name'))
        manager_email = str(x.get('manager_email'))
        adi_manageable = str(x.get('adi_manageable'))
        adi_guid = str(x.get('adi_guid'))
        joined_on = str(x.get('joined_on'))
        last_sign_in = str(x.get('last_sign_in'))
        status = str(x.get('status'))
        organization = str(x.get('organization'))
        department = str(x.get('department'))
        language = str(x.get('language'))
        comment = str(x.get('comment'))
        employee_start_date = str(x.get('employee_start_date'))
        archived_at = str(x.get('archived_at'))
        custom_field_1 = str(x.get('custom_field_1'))
        custom_field_2 = str(x.get('custom_field_2'))
        custom_field_3 = str(x.get('custom_field_3'))
        custom_field_4 = str(x.get('custom_field_4'))
        custom_date_1 = str(x.get('custom_date_1'))
        custom_date_2 = str(x.get('custom_date_2'))
        current_risk_score = str(x.get('current_risk_score'))
        groups = str(x.get('groups'))[1:][:-1]
        Userinfo = [user_id, employee_number, first_name, last_name, job_title, email, phish_prone_percentage, phone_number, extension, mobile_phone_number, location, division, manager_name, manager_email, adi_manageable, adi_guid, joined_on, last_sign_in, status, organization, department, language, comment, employee_start_date, archived_at, custom_field_1, custom_field_2, custom_field_3, custom_field_4, custom_date_1, custom_date_2, current_risk_score, groups]
        Users.append(Userinfo)

try:
    os.remove("KB4Users.csv")

except:
    pass


with open('C:/Users/x-geisc32sa/Desktop/KB4Users.csv', mode='w', newline='', encoding="utf-8") as User_File:
    User_writer = csv.writer(User_File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    User_writer.writerow(['User ID', 'Employee Number', 'First Name', 'Last Name', 'Job Title', 'Email', 'Phish Prone Percentage', 'Phone Number', 'Extension', 'Mobile Phone Number', 'Location', 'Division', 'Manager Name', 'Manager Email', 'ADI Managable', 'ADI Guide', 'Joined On', 'Last Sign On', 'Status', 'Orginization', 'Department', 'Language', 'Comment', 'Employee Start Date', 'Archived At', 'custom_field_1', 'custom_field_2', 'custom_field_3', 'custom_field_4', 'custom_date_1', 'custom_date_2', 'Current Risk Score', 'Groups'])

    for x in Users:
        User_writer.writerow([x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25], x[26], x[27], x[28], x[29], x[30], x[31], x[32]])

User_File.close()

