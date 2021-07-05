import requests


def test_uploads():

	file = '/Users/fox/Desktop/fulllog/FOC22401H1B181009163824.txt'

	url = "http://127.0.0.1:5002/fullog"
   
	files = {'file':open(file,'rb')}

	print(files)
	response = requests.request("POST", url, files=files)
	print(response.text)

test_uploads()
