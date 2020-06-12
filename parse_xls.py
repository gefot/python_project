# apt-get install python3-pandas
# apt-get install python3-xlrd

from pandas import *
import pprint

xls = ExcelFile('export_list.xlsx')
df = xls.parse(xls.sheet_names[0])
df_dict = df.to_dict()
# pprint.pprint(df_dict)

# print(df_dict['First Name'])
# print(df_dict['Last Name'])
# print(df_dict['Ext'])
# print(df_dict['DID'])
# print(df_dict['Site'])
# print(df_dict['Type'])

users = {}

# Construct dictionary from XLS
for i in df_dict['Ext']:
    # print("{} - {}".format(i, df_dict['Ext'][i]))
    try:
        my_extension = str(int(df_dict['Ext'][i]))
        my_type = str(df_dict['Type'][i])
        if my_type != "User Extension" and my_type != "Hunt Group" and my_type != "Distribution List" and my_type != "Paging Group":
            continue
    except:
        continue
    users[my_extension] = {}

    try:
        my_firstname = str(df_dict['First Name'][i])
        if my_firstname != "nan":
            users[my_extension]["FirstName"] = my_firstname
        else:
            users[my_extension]["FirstName"] = ""
    except:
        users[my_extension]["FirstName"] = ""

    try:
        my_lastname = str(df_dict['Last Name'][i])
        if my_lastname != "nan":
            users[my_extension]["LastName"] = my_lastname
        else:
            users[my_extension]["LastName"] = ""
    except:
        users[my_extension]["LastName"] = ""

    try:
        my_did = str(int(df_dict['DID'][i]))

        if my_did != "":
            users[my_extension]["DID"] = my_did
        else:
            users[my_extension]["DID"] = ""
    except:
        users[my_extension]["DID"] = ""

    try:
        my_site = str(df_dict['Site'][i])
        if my_site != "nan":
            users[my_extension]["Site"] = my_site
        else:
            users[my_extension]["Site"] = ""
    except:
        users[my_extension]["Site"] = ""

    try:
        my_type = str(df_dict['Type'][i])
        if my_type != "nan":
            users[my_extension]["Type"] = my_type
        else:
            users[my_extension]["Type"] = ""
    except:
        users[my_extension]["Type"] = ""


print("\n\n===================================\n\n")
pprint.pprint(users)
print(len(users))

