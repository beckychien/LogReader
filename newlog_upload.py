import requests


def test_uploads():

	file = '/Users/fox/Desktop/newlog/73-17637-11-180909083120-FCH2235714J'

	url = "http://10.132.46.138:5002/newlog"
   
	files = {'file':open(file,'rb')}

	print(files)
	response = requests.request("POST", url, files=files)
	print(response.text)

test_uploads()