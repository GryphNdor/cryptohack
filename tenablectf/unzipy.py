#!/usr/bin/env python3

from zipfile import ZipFile
import os

dir_name = "./"
extension = ".zip"

print("[*]Extracting")



#os.chdir(dir_name) # change directory from working dir to dir with files

# loop through items in dir
i = 128
while(1):
	try:
		print(f"Zip no: {i}")
		for item in os.listdir(dir_name):
			# check for ".zip" extension 
			if item.endswith(extension): 
				# get full path of files
				file_name = os.path.abspath(item) 
				# create zipfile object
				
				zip_ref = ZipFile(file_name) 
				
				# extract file to dir
				try:
					zip_ref.extractall(pwd=b'0')
				except:
					zip_ref.extractall(pwd=b'1') 
				
				zip_ref.close()
				os.rename(file_name, f"{file_name}_DONE") 
				#os.remove(file_name)
				i-=1 
			else:

	except:
		print("Nothng left to unzip")
		exit(1)