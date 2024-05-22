# week4 : YOLOv8 Object Tracking (Cars) & Training
</br>

* __參考 [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/quickstart/#use-ultralytics-with-python), 實作物件追蹤( classes[2] = 'car' ).__
</br>

## (1/2) YOLOv8 Object Tracking (Cars)

<div class="center"><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/ezgif-3-0c627c0921.gif" width=600 ></div>

</br></br></br>
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-20%20at%2015.06.49%402x.png" width=800 ></div>


### 創建環境 + 安裝package.
  ```
  conda create -n yo5 python=3.9.13
  conda activate yo5
  pip install ultralytics
  cd ultralytics
  ```
  * 根據規格裝PyTorch
  * 我是`pip3 install torch torchvision torchaudio`

</br></br></br>

### 實作方式-CLI
* `yolo predict model=yolov8n-seg.pt source='/Users/wsl/work/mvc/week4/argoverse.mp4' imgsz=320 classes=2`
* 第一次執行會載 `yolov8n-seg.pt`。
* 產生的影片會在 `../runs/segment/predict/` 裡面。
</br></br></br>
### 實作方式-Python
* yolov8_car.py
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-20%20at%2017.47.10%402x.png" width=800 ></div>
</br>
* 產生的結果同CLI。
</br></br></br>
</br></br></br>

## (2/2) YOLOv8 Training
</br>

### Preparing Our Dataset

* __在roboflow選擇關鍵字為`volleyball`的dataset。__
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.51.20%402x.png" width=800 ></div>
</br></br>

* __choose "show download code" & copy code chunk__
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.52.48%402x.png" width=400 ></div>
</br></br>

* __參考[train-yolov8-object-detection-on-custom-dataset.ipynb](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=jC4EwNJCl8cr)，使用colab作為訓練環境。__
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.56.47%402x.png" width=800 ></div>
</br></br></br>

### Training
</br>

* __貼上由roboflow載入dataset的程式碼片段 & 執行__
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.59.50%402x.png" width=800 ></div>
</br></br>

* __訓練完成 & 模型結果存於`/content/runs/detect/train/weights/best.pt`__
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2005.02.01%402x.png" width=800 ></div>
</br></br>

* __測試集的準確率__
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2005.03.00%402x.png" width=400 >
     <img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2005.03.23%402x.png" width=400 ></div>
</br></br></br>
</br></br></br>

### Predict 
</br>


#### 排球比賽中的截圖(照片可以成功追蹤) &nbsp; &nbsp; &nbsp; &nbsp; 影片

<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/runs/detect/predict3/IMG_DC99C3FA3F11-1.jpeg" width=350 >
     <img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/ezgif-7-218a511bc4.gif" width=350 ></div>
</br></br>

#### 網前，近距離

<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/ezgif-3-4a4d719c9d.gif" width=800 ></div>


</br></br></br></br></br></br>



一開始我先用youtube找一段比賽影片，但發現正式比賽太多干擾的資訊，所以裁切邊框，但還是追蹤失敗。
想說可能是其他顏色干擾，再選了一段攝影機跟著球的片段，且除了球沒有其他大面積的黃色，也失敗。
想說截圖丟進去看看，發現這種高速比賽我不管怎麼截圖，排球都會糊掉，可能是前面失敗的原因。
改用一段精彩瞬間慢動作回放的影片，結果一開始很成功，後來球遠離攝影機以及球速變快的時候就追蹤不到了。
結論：影片球速太快，排球太小(離攝影機太遠) 都會影響追蹤成功與否。





