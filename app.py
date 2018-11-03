import requests
import json
import os, shutil
import time,datetime

url='http://127.0.0.1:5002/data/'
path=os.path.abspath("..")+"/fulllog/"
for f in os.listdir(path):
	requst_url=url+f
	# requst_url=url+''
	print(requst_url)
	try:
		json_data=requests.post(requst_url)
		# json_data=requests.get(requst_url)
		if(json_data.status_code==200):
			data=json_data.json()
			if(data.get('result')=='Success'):
				print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' ['+str(json_data.status_code)+']:'+f+' parsing success')
			# shutil.move(path+f,os.path.abspath("..")+"/processedlog/")

		else:
			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' ['+str(json_data)+']:'+f+' parsing failed')
		time.sleep(0.5)

	except Exception as error:
		print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' error:'+str(error))  