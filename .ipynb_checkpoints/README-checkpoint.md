

# CPU OpenCV 人脸检测器

本文档演示了如何使用 OpenCV 库实现人脸检测并提取感兴趣区域（ROI）。

## 1. 导入 OpenCV 库

```python
import cv2
```

## 2. 加载人脸检测器

```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
```

## 3. 加载图像

```python
image = cv2.imread('./example.jpg')
```


## 4. 转换图像为灰度图

```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

## 5. 在灰度图上检测人脸

```python
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
```

## 6. 提取人脸 ROI 并保存

```python
for idx, (x, y, w, h) in enumerate(faces):
    roi = image[y:y+h, x:x+w]
    cv2.imwrite(f'Face_{idx+1}.jpg', roi)
```

---

该文档提供了代码的逐步说明和注释，包括导入库、加载人脸检测器、加载图像、转换为灰度图、检测人脸、提取人脸 ROI 并保存的步骤。在第6步中，将每个检测到的人脸 ROI 提取并保存为单独的图像文件，文件名为 "Face_1.jpg"、"Face_2.jpg" 等，以此类推。