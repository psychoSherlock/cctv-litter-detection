# CCTV Based Litter Detection
### IEDC TechXcel Challange

We used [Yolov8](https://github.com/ultralytics/ultralytics) for training our models:
We used the [UAVVase](https://github.com/PUTvision/UAVVaste) as the dataset

## Results
We had not any access to computing powers so the outputs are not accurate yet.

### YOLOv8n 50 Epochs
#### Without any threshold

![image](https://github.com/psychoSherlock/cctv-litter-detection/assets/81918189/8f4ef07a-2541-4400-b5ef-f5bb3ddd0f54)

#### With threshold, and highest confidence

![image](https://raw.githubusercontent.com/psychoSherlock/cctv-litter-detection/master/result_highest_conf.jpg)

![image](https://raw.githubusercontent.com/psychoSherlock/cctv-litter-detection/master/output_test1.jpg)

![image](https://raw.githubusercontent.com/psychoSherlock/cctv-litter-detection/master/output_test3.jpg)


We then tried the same algorithm with different models. But as the dataset is not sufficient enought, the model loss too much data as we increased the epochs. As a result, 100 to 300 epochs resulted in more overfitting predictions than the 50 epochs.

We also tried increasing the dataset by a process called data augmentation. This had a little effect on the data and still resulted in the losses.

We also changed the learning model from nano to small and medium ones but as the models increased, the loss increased. So it was clear that we needed a better dataset to increase the accuracy.


##### Small, with 200 epochs

![output_s_test1](https://github.com/psychoSherlock/cctv-litter-detection/assets/81918189/28099217-0b81-4a3c-8c63-a66b9d59b759)


![output_s_200pleasework](https://github.com/psychoSherlock/cctv-litter-detection/assets/81918189/273bee32-0de6-4252-8676-120d57a48679)


##### Small, with 30 epochs

![output_s_30test1](https://github.com/psychoSherlock/cctv-litter-detection/assets/81918189/36938437-84e4-4102-81bb-6f66d2f2afa0)


## Resources for training.

We tried running few models on google colab with its GPU. Its faster but they kick off the users very often resulting in loss in the data. Fortunately, we saved it to google drive and used Kaggle for training, with its GPU.


# Human Detection

Human detection was straight forward as the COCO dataset already contains the human models. We were able to put up the bare yolo nano model which was trained on YOLO. Class number 0 would give the humans. We then combined both the models to identify humans and the litters.



# Citation
Thanks for the dataset
```
@Article{rs13050965,
AUTHOR = {Kraft, Marek and Piechocki, Mateusz and Ptak, Bartosz and Walas, Krzysztof},
TITLE = {Autonomous, Onboard Vision-Based Trash and Litter Detection in Low Altitude Aerial Images Collected by an Unmanned Aerial Vehicle},
JOURNAL = {Remote Sensing},
VOLUME = {13},
YEAR = {2021},
NUMBER = {5},
ARTICLE-NUMBER = {965},
URL = {https://www.mdpi.com/2072-4292/13/5/965},
ISSN = {2072-4292},
DOI = {10.3390/rs13050965}
}
```
