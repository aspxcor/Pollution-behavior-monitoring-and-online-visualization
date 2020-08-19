#TransImageTo50px
#转换图片大小为50*50，cascade分类器数据集预处理
from PIL import Image 
count=0
for count in range(1,65):
    infile = 'C:\FFOutput\A ('+str(count)+').jpg'
    outfile = 'C:\FFOutput\\'+str(count)+'.jpg'
    im = Image.open(infile)
    (x,y) = im.size #read image size
    x_s = 50 #define standard width
    y_s = 50 #calc height based on standard width
    out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
    out.save(outfile)