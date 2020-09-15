# Counting-Objects-Using-YOLOv4-Object-Detection-and-TensorFlow
  
This repository aims to both detect custom images as well as count them. Project is divided into three phases. 

:sparkle:	**Phase 1:** Yolo Model is created using pretrained yolov4 weights, yolo4 config files and customized dataset (containing pizza and fork images)  
:sparkle:	 **Phase 2:** Yolo created model is converted into tensorflow frozen model  
:sparkle:	**Phase 3:** Detectiion of objects in image and their counting is carried out.  

## Why YOLOV4 not v1, v2 and v3  
YOLOv4’s architecture is composed of CSPDarknet53 as a backbone, spatial pyramid pooling additional module, PANet path-aggregation neck and YOLOv3 head [Source What’s new in YOLOv4?](https://towardsdatascience.com/whats-new-in-yolov4-323364bb3ad3). CSPDarknet53 is a novel backbone that can enhance the learning capability of CNN. The spatial pyramid pooling block is added over CSPDarknet53 to increase the receptive field and separate out the most significant context features. Instead of Feature pyramid networks (FPN) for object detection used in YOLOv3, the PANet is used as the method for parameter aggregation for different detector levels [Source What’s new in YOLOv4?](https://towardsdatascience.com/whats-new-in-yolov4-323364bb3ad3).   

## Architecture for this project  
* **Dataset used:** Dataset has been downloaded from Open Image Dataset which contains 600 classes and more than 1,700,000 images. Link for the Dataset is [Open Image Dataset v4](https://storage.googleapis.com/openimages/web/index.html). Dataset is very huge and I had made the code for two classes named as Pizza and Fork. To download images for specific classes, I followed the repository [OIDv4_Toolkit](https://github.com/EscVM/OIDv4_ToolKit). Look at the repo and each step is clearly mentioned how to do this. Once you clone the above github repository please create the virtualenv and install the requirements mentioned in the reposiotry.  









