import os # importing library for operating system
current_path = os.getcwd() # getting the current path of the directory
# this function will list all the files in the current directory
list_files = os.listdir(current_path)

"""
Code to rename the filenames in the dir
Names of files as well as labels downloaded from Open Images Dataset v4 are something like 0fdea8a716155a8e
The below script converts it into the numbers such as 1,2,3,4 and so on which is more readable
Also for pizza images Pizza is prefix with the images and same holds true for fork images also
"""
count=200 # since each folder pizza and fork contains 200 images each both jpg and .txt
for each_file in list_files:
	if each_file.endswith('jpg'):
		filename, extension = os.path.splitext(each_file)
		tmp = filename # temporary variable to store the filename
		overall_path_jpg = os.path.join(current_path, each_file) # getting the overall path
		file_txt = tmp + '.txt'
		overall_path_txt = os.path.join(current_path, file_txt)
		jpg_new_name = "Pizza" + "_" + str(count) + ".jpg"
		txt_new_name = "Pizza" + "_" + str(count) + ".txt"
		destination_path_jpg = os.path.join(current_path, jpg_new_name)
		destination_path_txt = os.path.join(current_path, txt_new_name)
		os.rename(overall_path_jpg, destination_path_jpg)
		os.rename(overall_path_txt, destination_path_txt)
		count+=1
