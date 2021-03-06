# Counting-Objects-Using-YOLOv4-Object-Detection-and-TensorFlow  
![detection1](https://user-images.githubusercontent.com/39157936/93322424-edcd6100-f830-11ea-92a9-3e001605e5c5.png)
  
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
* **Creating config file inside the custom folder**: config file is created in the custom folder. There are some changes which one has to do. I am mentioning below which is taken from [AlexeyAB darknet](https://github.com/AlexeyAB/darknet). These are as below  
   * change line batch to batch=64  
   * change line subdivisions to subdivisions=16  
   * change line max_batches to (classes*2000)  
   * change line steps to 80% and 90% of max_batches  
   * set network size width=416 height=416 or any value multiple of 32
   * change line classes=n to your number of objects in each of 3 yolo-layers (n is number of classes)  
   * change [filters=255] to filters=(classes + 5)x3 in the 3 [convolutional] before each [yolo] layer, keep in mind that it    only has to be the last [convolutional] before each of the [yolo] layers. Please write the integer value after caliculation not  (classes + 5)x3. In my case there are 2 classes and hence the value is 2+5*3=21. Please check the custom.cfg file in the repo to know the things better  
* **.data**: This will contains classes, train, valid, names and backup. backup is the folder where trained model weights are stored. 
* **.names**: custom.names contains names of the classes.
* **Training the yolov4 model**: Since all the changes has been made, now it is time to train the model using the below command   
```
./darknet detector train custom.data custom.cfg yolov4.conv.137   

```  
Download yolov4.conv.137 from  the [link](https://drive.google.com/file/d/1JKF-bdIklxOOVy-2Cr5qdvjgGpmGfcbp/view). Reference for this one is [AlexeyAB darknet](https://github.com/AlexeyAB/darknet)   
* During Training, I got the below loss rate at 4000 iterations. Please see the results from the below chart.  
Training is stopped at 4000 iterations and weights can be downloaded using the link [custom_4000.weights](https://drive.google.com/file/d/1KdXcpRJm9NkOgQhd00HeqZHHMujPG4Ok/view?usp=sharing)  
![chart_kitchen](https://user-images.githubusercontent.com/39157936/93302966-63790300-f818-11ea-9462-393206e78101.png)  

* **Converting the yolo model into tensorflow model**: First of all to accomplish this step, please download the below repository [the AI GuysCode](https://github.com/theAIGuysCode/yolov4-custom-functions) and install all the requirements. I have installed for gpu. I need cuda 10.1 and nvidia-drivers greater than or equal to 418. Please read from [here](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html).   
```
python save_model.py --weights ./data/custom_4000.weights --output ./checkpoints/yolov4-416 --input_size 416 --model yolov4 
```  
Note: Use custom_4000.weights and put the name of classes in core/config.py files there which is custom.names. If everything goes well, one will get the checkpoints which is tensorflow frozen model.  
* **Detection only**: Use the below code for detectiing objects only    
```
python3 detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/pizza_fresca.jpg
```  
* **Some changes**: To display the classes of each object which one needs to count, please make the change as "To count the number of objects for each individual class of your object detector you need to add the custom flag "--count" as well as change one line in the detect.py or detect_video.py script. By default the count_objects function has a parameter called by_class that is set to False. If you change this parameter to True it will count per class instead"  
```
python3 detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/pizza-and-fork.jpg --count  
```   
* **Cropping Detected Region and Finding bounding boxes of each class:**  Run the below code for this  
```
python3 detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/pizza-and-fork.jpg --crop      
```  
Also please look at the below screenshot to find the bounding boxes of each class  
![cropping_results](https://user-images.githubusercontent.com/39157936/93324522-a8f6f980-f833-11ea-8e53-3059b21ada3b.png)


If everything goes fine, you will get results  
Happy Coding!!!


