import subprocess
import sys
import os
import json
try:
   import pip
except ImportError:
   cmd = "easy_install pip"
   os.system(cmd)
   print("Pip Installed")


input_file=open('rq.json', 'r')
json_decode=json.load(input_file)
dependencies = []
dependencies = json_decode["Dependencies"]
failed = []


for x in dependencies:
	flag=1
	try:
		cmd = "python -m pip install "+x
		flag = os.system(cmd)
	except ImportError:
		print("Check the depenencies"+x)
	#flag = 0 if success
	if(flag!=0):
		failed.append(x)
		
		


if not failed:
  print("Success")
else:
	print("Packages failed to install")
	for item in failed:
		print(item)

