import pandas as pd
import os
"""
train-annotations-bbox.csv will be downloaded if you go through point Dataset Used Under Implementation of this project
in readme File
"""
f=pd.read_csv("/yolo_model/darknet/OIDv4_ToolKit/OID/csv_folder/train-annotations-bbox.csv")
"""
There is another files downloaded (if you go through point Dataset Used Under Implementation of this project) called
as class-descriptions-boxable.csv. From this file the code for fork is /m/0dt3t
"""
# Reference for this code can be taken from https://github.com/WyattAutomation/Train-YOLOv3-with-OpenImagesV4
numClasses = ['/m/0dt3t']
u = f.loc[f['LabelName'].isin(numClasses)]
keep_col = ['LabelName','ImageID','XMin','XMax','YMin','YMax']
new_f = u[keep_col]
new_f['ClassNumber'] = new_f['LabelName']
# label 0 is assigned to Fork
new_f.loc[new_f['LabelName'] == '/m/0dt3t', 'ClassNumber'] = 0
new_f['width'] = new_f['XMax'] - new_f['XMin']
new_f['height'] = new_f['YMax'] - new_f['YMin']
new_f['x'] = (new_f['XMax'] + new_f['XMin'])/2
new_f['y'] = (new_f['YMax'] + new_f['YMin'])/2
keep_col = ['ClassNumber','ImageID','x','y','width','height']
new_f_2 = new_f[keep_col]
for root, dirs, files in os.walk("."):
	for filename in files:
		if filename.endswith(".jpg"):
			fn = filename[:-4]
			nf = new_f_2.loc[new_f_2['ImageID'] == fn]
			keep_col = ['ClassNumber','x','y','width','height']
			new_nf = nf[keep_col]
			print(new_nf)
			# saving the txt file containing all the labels for fork images
			imgpath = "/yolo_model/darknet/OIDv4_ToolKit/OID/Dataset/train/Fork_labels/" + fn + ".txt"
			print(imgpath)
			new_nf.to_csv(imgpath, index=False, header=False, sep=' ')
