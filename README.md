# Counting-Objects-Using-YOLOv4-Object-Detection-and-TensorFlow
  
This repository aims to both detect custom images as well as count them. Project is divided into three phases. 

:sparkle:	**Phase 1:** Yolo Model is created using pretrained yolov4 weights, yolo4 config files and customized dataset (containing pizza and fork images)  
:sparkle:	 **Phase 2:** Yolo created model is converted into tensorflow frozen model  
:sparkle:	**Phase 3:** Detectiion of objects in image and their counting is carried out.  

## Why YOLOV4 not v1, v2 and v3  
YOLOv4’s architecture is composed of CSPDarknet53 as a backbone, spatial pyramid pooling additional module, PANet path-aggregation neck and YOLOv3 head [Source What’s new in YOLOv4?](https://towardsdatascience.com/whats-new-in-yolov4-323364bb3ad3). CSPDarknet53 is a novel backbone that can enhance the learning capability of CNN. The spatial pyramid pooling block is added over CSPDarknet53 to increase the receptive field and separate out the most significant context features. Instead of Feature pyramid networks (FPN) for object detection used in YOLOv3, the PANet is used as the method for parameter aggregation for different detector levels [Source What’s new in YOLOv4?](https://towardsdatascience.com/whats-new-in-yolov4-323364bb3ad3).   

## Implementation for this project  
* **Dataset used:** Dataset has been downloaded from Open Image Dataset which contains 600 classes and more than 1,700,000 images. Link for the Dataset is [Open Image Dataset v4](https://storage.googleapis.com/openimages/web/index.html). Dataset is very huge and I had made the code for two classes named as Pizza and Fork. To download images for specific classes, I followed the repository [OIDv4_Toolkit](https://github.com/EscVM/OIDv4_ToolKit). Look at the repo and each step is clearly mentioned how to do this. Once you clone the above github repository please create the virtualenv and install the requirements mentioned in the reposiotry.I have used 200 images for both pizza and fork 
* **Labels creation:** Next Step was to create label for each image. For this I have used two python files named as Fork.py and pizza.py which has been created with the help of Wyatt Automation: [Training YOLOV3 with OpenImagesv4](https://github.com/WyattAutomation/Train-YOLOv3-with-OpenImagesV4). Please take care of the path you choose to save the labels corresponding to each folder.  
* **Renaming_filenames and labels:** Filenames and labels has been renamed from 0 to 399 integer values using the renaming_filename.py script. i am sharing the link where filesnames and labels can be downloaded directly and once can save himself/herself from above step. Here is the [link](https://drive.google.com/drive/folders/1XGLrIRB16pdrV7VJ3t6c9HGfesu8rkPp?usp=sharing)  
* **Download AlexeyAB darknet Repository:** Please download the AlexeyAB darknet repository using this [link](https://github.com/AlexeyAB/darknet). Along with that you need to install darknet in your system. Darknet can be installed both for cpu and gpu. Please follow this [link](https://pjreddie.com/darknet/install/). Once the repo is downloaded  please create the custom folder in the repository with the below files  
   * cfg containing cfg file for yolov4 custom dataset project
   * images folder containing images and labels  
   * .data file containing path for train, valid, names and backup. We will create train and valid files soon    
   * .names file containing names of labels such as pizza and fork in my case
   * .process.py: It will create train.txt and valid.txt  
   * test.txt: Path of testing images  
   * train.txt: Path of training images  
* **Inside custom folder**: Inside custom folder place images which contains images and labels. Inside this folder place the file proces.py [reference](https://github.com/WyattAutomation/Train-YOLOv3-with-OpenImagesV4) and run this. One will get train.txt an test.txt outside the custom folder. Now we need to make cfg for custom dataset, .data file and .names file which will be discussed in the next steps 











