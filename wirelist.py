import requests
import json
import os, shutil
import time,datetime

url='http://127.0.0.1:5002/Wirelist/73-18275-04'

print(url)
try:
	json_data=requests.post(url)
	if(json_data.status_code==200):
		data=json_data.json()
		if(data.get('result')=='Success'):
			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' ['+str(json_data.status_code)+']:parsing success')
	
	else:
		print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' ['+str(json_data.status_code)+']:parsing failed')
	time.sleep(2)

except Exception as error:
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' error:'+str(error))  