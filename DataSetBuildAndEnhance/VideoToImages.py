#VideoToImages
#将我们实拍视频按一定帧率截取成图片，收入样本集
import cv2
import os

# 要提取视频的文件名，去除后缀
sourceFileName = r'C:\Users\NightFury\Desktop\video\x6'
video_path = os.path.join("", "data", sourceFileName+'.mp4')

times = 0
# 设置提取视频的频率
frameFrequency = 50
# 输出文件夹
outPutDirName = 'video/'

if not os.path.exists(outPutDirName):
    os.makedirs(outPutDirName)
camera = cv2.VideoCapture(video_path)
while True:
    times += 1
    res, image = camera.read()
    if not res:
        print('not res , not image')
        break
    if times % frameFrequency == 0:
        cv2.imwrite(outPutDirName + str(times)+'.jpg', image)
        print(outPutDirName + str(times)+'.jpg')

print('图片提取结束')
camera.release()
