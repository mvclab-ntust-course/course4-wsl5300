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
* `yolo predict model=yolov8n-seg.pt source='/Users/wsl/work/mvc/week4/argoverse.mp4' imgsz=320 **classes=2**`
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
