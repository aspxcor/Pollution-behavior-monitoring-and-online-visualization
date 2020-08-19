from django.shortcuts import render
from django.http import HttpResponse
from .models import  *
from django.http import JsonResponse
from django.forms.models import model_to_dict
import os
from cv2 import cv2 as cv
from matplotlib import pyplot as plt


def index(request):
    return render(request, 'index.html')

def index_temp(request):
    return render(request, 'index_temp.html')


def people_origin_get(request):
    people_origin_temp = peolple_origin.objects.all()
    people_origin_data = []
    for data in people_origin_temp:
        dict_data = model_to_dict(data)
        del dict_data['id']
        dict_data['name'] = dict_data['origin_province']
        dict_data['value'] = dict_data['people_count']
        del dict_data['origin_province']
        del dict_data['people_count']
        people_origin_data.append(dict_data)
    return JsonResponse({'data':  people_origin_data})

def  crime_analyze_get(request):
    temp = crime_analyze.objects.all()
    crime_analyze_data = []
    for data in temp:
        dict_data = model_to_dict(data)
        del dict_data['id']
        dict_data['name'] = dict_data['type_name']
        dict_data['value'] = dict_data['type_value']
        del dict_data['type_name']
        del dict_data['type_value']
        crime_analyze_data.append(dict_data)
    return JsonResponse({'data': crime_analyze_data})

def  age_distribution_get(request):
    temp = age_distribution.objects.all()
    age_distribution_data = []
    for data in temp:
        dict_data = model_to_dict(data)
        del dict_data['id']
        dict_data['name'] = dict_data['age_distribution_type']
        dict_data['value'] = dict_data['age_distribution_value']
        del dict_data['age_distribution_type']
        del dict_data['age_distribution_value']
        age_distribution_data.append(dict_data)
    return JsonResponse({'data': age_distribution_data})
def  time_line_get(request):
    temp = time_line_statistics.objects.all()

    time_line_xAxis =[]
    time_line_value = []
    for data in temp:
        dict_data = model_to_dict(data)
        time_line_xAxis.append(dict_data['time_line_statistics_type'])
        time_line_value.append(dict_data['time_line_statistics_value'])

    return JsonResponse({'data_xAxis': time_line_xAxis,'data_value':time_line_value})


def test01(request):
    file_obj=request.POST.get('url')
    print(file_obj)
    return JsonResponse({'data':'/static/user/new/demo.jpg'})
## 污水排放检测
def upload(request):
    return render(request, "upload.html")

# def upload_file(request):
#     username = request.POST.get('username')
#     f1 = request.FILES.get('f1')    # 获取文件对象
#     print(username, f1)

#     with open(f1.name, 'wb') as f:
#         for item in f1.chunks():    # 循环文件对象，并分次写入
#             f.write(item)
#     ret = {'status': True, 'data': request.POST.get('username')}
#     import json
#     return HttpResponse(json.dumps(ret)) 

def upload_file(request):
    # username = request.POST.get('username')
    f1 = request.FILES.get('f1')
    # print(username, f1)
    print(f1)
    import os
    img_path = os.path.join('AI/CV/', f1.name.replace(" ",""))     # 注意：文件名有空格不能在页面上显示
    with open(img_path, 'wb') as f:
        for item in f1.chunks():
            f.write(item)
    ret = {'status': True, 'data': img_path}    # 把图片文件的路径返回给前端
    #ret = {'status': True, 'data': request.POST.get('username')}
    import json
    return HttpResponse(json.dumps(ret))

def object_detection(request):

    img = cv.imread('AI/CV/test.jpg')
    # img = cv.imread('temp01.jpg')
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #
    engine = cv.CascadeClassifier('AI/CV/cascade.xml')
    # engine.load('C:/Users/23672/Desktop/实习文件/mysite/AI/CV/cascade.xml')
    pipeline = engine.detectMultiScale(img, scaleFactor=1.3, minNeighbors=100, minSize=(100, 100))

    for (x, y, w, h) in pipeline:
        img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    # cv.imshow('img', img)
    cv.imwrite('static/AI/result.jpg',img)
    # plt.figure()
    # plt.imshow(img)
    # plt.imshow(img)
    # print('已识别排水管位置')
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    x = 1

    return HttpResponse({"data":1})

