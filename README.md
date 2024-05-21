# week4 : YOLOv8 Object Tracking (Cars) & Training
## (1/2) YOLOv8 Object Tracking (Cars)

* 搜尋yolov8, git clone.
  <div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-20%20at%2015.06.49%402x.png" width=800 ></div>

* 參考 [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/quickstart/#use-ultralytics-with-python), 實作物件追蹤( classes[2] = 'car' ).

### 創建環境 + 安裝package.
  ```
  conda create -n yo5 python=3.9.13
  conda activate yo5
  pip install ultralytics
  cd ultralytics
  ```
  * 根據規格裝PyTorch
  * 我是`pip3 install torch torchvision torchaudio`

  
### 實作方式-CLI
* `yolo predict model=yolov8n-seg.pt source='/Users/wsl/work/mvc/week4/argoverse.mp4' imgsz=320 classes=2`
* 第一次執行會載 `yolov8n-seg.pt`。
* 產生的影片會在 `../runs/segment/predict/` 裡面。
</br></br>
### 實作方式-Python
* yolov8_car.py
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-20%20at%2017.47.10%402x.png" width=800 ></div>
</br>
* 產生的結果同CLI。
</br></br></br>


## (2/2) YOLOv8 Training

### **Preparing Our Dataset**

* 在roboflow選擇關鍵字為“volleyball”的dataset。
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.51.20%402x.png" width=800 ></div>
</br></br>

* choose "show download code" & copy code chunk
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.52.48%402x.png" width=400 ></div>
</br></br>

* 參考[train-yolov8-object-detection-on-custom-dataset.ipynb](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=jC4EwNJCl8cr)，使用colab作為訓練環境。
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.56.47%402x.png" width=800 ></div>
</br></br></br>

### **Training**
  
* 貼上由roboflow載入dataset的程式碼片段 & training
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2004.59.50%402x.png" width=800 ></div>
</br></br>

* 訓練完成 & 模型結果存於“”
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2005.02.01%402x.png" width=800 ></div>
</br></br>

* 確認test的準確率
<div><img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2005.03.00%402x.png" width=400 >
     <img src="https://github.com/mvclab-ntust-course/course4-wsl5300/blob/main/photos/CleanShot%202024-05-22%20at%2005.03.23%402x.png" width=400 ></div>
</br></br></br>

### **Predict**

* 預測的圖片

* 預測的影片







