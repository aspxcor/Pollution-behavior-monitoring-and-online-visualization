import cv2
import os
import torch
from PIL import Image
from torchvision import transforms


def object_detection_show(filename, cla1, cla2, num):
    img = cv2.imread(filename)

    # 加载训练好的模型
    engine = cv2.CascadeClassifier('cascade.xml')
    pipeline = engine.detectMultiScale(img, scaleFactor=1.1,
                                       minNeighbors=30, minSize=(120, 120))

    for (x, y, w, h) in pipeline:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 标注stage2分类结果，有无排水
        # 0 is not, 1 is yes
        if cla1 == 1:
            text = "watering"
        else:
            text = 'no water'
        cv2.putText(img, text, (x, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
        # 标注stage3分类结果，清水还是污水
        # 0 is clean, 1 is dirty
        if cla1 == 1:
            if cla2 == 1:
                text = "dirty"
            else:
                text = 'clean'
            cv2.putText(img, text, (x, y + h),
                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imwrite('result/' + str(num) + '.jpg', img)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def object_detection_data(filename, gray_or_not, num):
    img = cv2.imread(filename)
    # 是否转化图片至灰度图
    if gray_or_not == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img = img

    # 加载训练好的模型
    engine = cv2.CascadeClassifier('cascade.xml')
    pipeline = engine.detectMultiScale(img, scaleFactor=1.1,
                                       minNeighbors=30, minSize=(120, 120))

    for (x, y, w, h) in pipeline:
        # 裁剪坐标为[y0:y1, x0:x1]
        cropped = img[y:y+w, x:x+w]
        cv2.imwrite('database/' + str(num) + '.jpg', cropped)


def predict_yes_not(img_path):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    # print('train_device:{}'.format(device.type))

    net = torch.load('model_yes_or_not')
    net = net.to(device)
    torch.no_grad()

    img = Image.open(img_path)
    transform = transforms.Compose([transforms.RandomResizedCrop(150),
                                    transforms.RandomHorizontalFlip(),
                                    transforms.ToTensor(),
                                    transforms.Normalize(
                                        mean=(0.485, 0.456, 0.406),
                                        std=(0.229, 0.224, 0.225))
                                    ])

    img = transform(img).unsqueeze(0)
    img_ = img.to(device)

    outputs = net(img_)
    _, predicted = torch.max(outputs, 1)
    # 0 is not, 1 is yes
    stage1_result = predicted[0].numpy()
    return stage1_result


def predict_clean_dirty(img_path):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    # print('train_device:{}'.format(device.type))

    net = torch.load('model_clean_or_dirty')
    net = net.to(device)
    torch.no_grad()

    img = Image.open(img_path)
    transform = transforms.Compose([transforms.RandomResizedCrop(150),
                                    transforms.RandomHorizontalFlip(),
                                    transforms.ToTensor(),
                                    transforms.Normalize(
                                        mean=(0.485, 0.456, 0.406),
                                        std=(0.229, 0.224, 0.225))
                                    ])

    img = transform(img).unsqueeze(0)
    img_ = img.to(device)

    outputs = net(img_)
    _, predicted = torch.max(outputs, 1)
    # 0 is clean, 1 is dirty
    stage2_result = predicted[0].numpy()
    return stage2_result


def process_all_stage(path):
    lines = os.listdir(path)
    i = 0
    for data in lines:
        file = path + '/' + data
        object_detection_data(file, 0, i)
        cla1 = predict_yes_not('database/' + str(i) + '.jpg')
        cla2 = predict_clean_dirty('database/' + str(i) + '.jpg')
        object_detection_show(file, cla1, cla2, i)
        print('FINISHED PICTURE ' + str(i))
        i += 1


with open('path.txt', 'r', encoding='utf-8') as f:
    file_path = f.readline()
process_all_stage(file_path)
