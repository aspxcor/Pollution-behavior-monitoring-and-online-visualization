# 管道出水数据集增强
import cv2
from imgaug import augmenters as iaa
import imgaug
import glob
import os
sometimes = lambda aug: iaa.Sometimes(0.5, aug)
seq = iaa.Sequential(
    [
        iaa.Fliplr(0.2), # 对20%的图像进行镜像翻转
        iaa.Flipud(0.2), # 对20%的图像做左右翻转
        sometimes(iaa.Crop(percent=(0, 0.1))), #对随机的一部分图像剪切，幅度为0到10%
        sometimes(iaa.Affine(                          #对一部分图像做仿射变换
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},#图像缩放为80%到120%之间
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, #平移±20%之间
            rotate=(-25, 25),   #旋转±45度之间
            shear=(-2, 2),    #剪切变换±16度，（矩形变平行四边形）
            order=[0, 1],   #使用最邻近差值或者双线性差值
            cval=(0, 255),  #全白全黑填充
            mode=imgaug.ALL    #定义填充图像外区域的方法
        )),
        iaa.SomeOf((0, 5),# 使用下面的0个到5个之间的方法增强图像
            [
                sometimes(# 将部分图像进行超像素的表示
                    iaa.Superpixels(
                        p_replace=(0, 1.0),
                        n_segments=(20, 200)
                    )
                ),
                iaa.OneOf([#用高斯模糊，均值模糊，中值模糊中的一种增强
                    iaa.GaussianBlur((0, 2.0)),
                    iaa.AverageBlur(k=(2, 7)), # 核大小2~7之间
                    iaa.MedianBlur(k=(3, 7)),
                ]),
                iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)),#锐化
                iaa.AdditiveGaussianNoise(                # 高斯噪声
                    loc=0, scale=(0.0, 0.05*255), per_channel=0.5
                ),
                sometimes(iaa.PiecewiseAffine(scale=(0.01, 0.05)))# 扭曲图像的局部
            ],
            random_order=True # 随机顺序
        )
    ],
    random_order=True # 随机顺序
)
imglist=[]
WSI_MASK_PATH = './1//'#存放图片的文件夹路径
paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.jpg'))
paths.sort()
count=0
for path in paths:
    count+=1
    img= cv2.imread(path)
    imglist.append(img)
    images_aug = seq.augment_images(imglist)
    name=str(count)+"Water.jpg"
    cv2.imwrite(name,images_aug[0])
    imglist.clear()