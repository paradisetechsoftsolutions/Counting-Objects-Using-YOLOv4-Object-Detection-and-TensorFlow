import glob, os
"""
Path set here is custom>images
images contains both labels and images
Aim is to make train.txt and test.txt which contains path of images 
Reference:     https://github.com/WyattAutomation/Train-YOLOv3-with-OpenImagesV4
"""
current_dir = '/yolo_model/darknet_tuned/OIDv4_ToolKit/OID/darknet/alex_folder/darknet/custom/images'
# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1