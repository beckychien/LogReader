import requests


def test_uploads():

	file = '/Users/fox/Desktop/newlog/73-17637-11-180909051904-FCH2235711V'

	url = "http://127.0.0.1:5002/newlog"
   
	files = {'file':open(file,'rb')}

	print(files)
	response = requests.request("POST", url, files=files)
	print(response.text)

test_uploads()
