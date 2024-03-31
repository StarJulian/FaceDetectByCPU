import cv2

# 加载人脸检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 加载图像/
image = cv2.imread('./examples/000001.jpg')

# 将图像转换为灰度图
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 在灰度图上检测人脸
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 在检测到的人脸周围画矩形框
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 显示结果图像
cv2.imwrite('./examples/Face_Detected.jpg', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
