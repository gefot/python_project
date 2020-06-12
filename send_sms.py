import pycurl
import json


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


### Main
sender = "15122290591"
receiver = "+15122290591"
sms_body = "Hello World!!!"
sms_status = send_sms_flowroute(sender, receiver, sms_body)
