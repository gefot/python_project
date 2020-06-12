# apt-get install python3-pandas
# apt-get install python3-xlrd

import pycurl
import json

import pandas
import pprint
from operator import itemgetter

####################################################################################################
def send_sms_flowroute(my_sender, my_receiver, text):

    try:
        pycurl_connect = pycurl.Curl()
        pycurl_connect.setopt(pycurl.URL, 'https://api.flowroute.com/v2/messages')
        pycurl_connect.setopt(pycurl.HTTPHEADER, ['Cache-Control: no-cache', 'Content-Type: application/json'])
        pycurl_connect.setopt(pycurl.POST, 1)
        pycurl_connect.setopt(pycurl.TIMEOUT_MS, 3000)
        my_data = {"to": my_receiver, "from": my_sender, "body": text}
        data = json.dumps(my_data)
        pycurl_connect.setopt(pycurl.POSTFIELDS, data)

        # Authentication
        username = "e0467a57"
        password = "8dbc56be68204eeba96a15adc513e5e4"
        creds = "{}:{}".format(username, password)
        pycurl_connect.setopt(pycurl.USERPWD, creds)
        pycurl_connect.perform()

        status_code = pycurl_connect.getinfo(pycurl.RESPONSE_CODE)
        if status_code != 200:
            return 0
        else:
            return 1

    except Exception as ex:
        print("send_sms exception: ", ex)
        raise Exception(ex)


####################################################################################################
def create_list_of_dicts_from_xls(xls_file):

    try:
        xls = pandas.ExcelFile(xls_file)
        df = xls.parse(xls.sheet_names[0])
        df_dict = df.to_dict()

        a_key = list(df_dict.keys())[0]
        len_of_columns = len(df_dict[a_key].keys())

        all_entries = []
        for i in range(len_of_columns):
            my_entry = {}
            for j in df_dict.keys():
                my_entry[j] = df_dict[j][i]
            all_entries.append(my_entry)

        return all_entries

    except Exception as ex:
        print("create_list_of_dicts_from_xls exception: ", ex)
        raise Exception(ex)


####################################################################################################
def normalize_shoretel_entries(all_entries):

    new_all_entries = []
    try:
        for entry in all_entries:
            if str(entry['First Name']) == "nan":
                entry['First Name'] = ""

            if str(entry['Last Name']) == "nan":
                entry['Last Name'] = ""

            if str(entry['Site']) == "nan":
                entry['Site'] = ""

            try:
                entry['Ext'] = int(entry['Ext'])
            except:
                entry['Ext'] = ""

            try:
                entry['DID'] = int(entry['DID'])
            except:
                entry['DID'] = ""

        for entry in all_entries:
            if entry['Type'] == "User Extension" or entry['Type'] == "Hunt Group":
                new_all_entries.append(entry)

        return new_all_entries

    except Exception as ex:
        print("normalize_shoretel_entries exception: ", ex)
        raise Exception(ex)


####################################################################################################
def create_xls_from_list_of_dicts(list_of_dicts):

    try:
        list_of_dicts_ordered = sorted(list_of_dicts, key=itemgetter('Site', 'Ext'))
        for dict in list_of_dicts_ordered:
            print(dict)

        # Create Pandas Dataframe
        my_length = len(list_of_dicts_ordered)
        excel_dict = {}
        excel_dict['Site'] = []
        excel_dict['Extension'] = []
        excel_dict['First Name'] = []
        excel_dict['Last Name'] = []
        excel_dict['DID'] = []
        for i in range(my_length):
            excel_dict['Site'].append(list_of_dicts_ordered[i]['Site'])
            excel_dict['Extension'].append(list_of_dicts_ordered[i]['Ext'])
            excel_dict['First Name'].append(list_of_dicts_ordered[i]['First Name'])
            excel_dict['Last Name'].append(list_of_dicts_ordered[i]['Last Name'])
            excel_dict['DID'].append(list_of_dicts_ordered[i]['DID'])

        pprint.pprint(excel_dict)
        df = pandas.DataFrame(excel_dict)
        writer = pandas.ExcelWriter('demo.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()

    except Exception as ex:
        print("create_xls_from_list_of_dicts exception: ", ex)
        raise Exception(ex)

