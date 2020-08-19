from django.urls import path
from . import views
from AI.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('people_origin_get/',people_origin_get),
    path('crime_analyze_get/',crime_analyze_get),
    path('age_distribution_get/', age_distribution_get),
    path('time_line_get/', time_line_get),

    path('index_temp/',index_temp),
    path('upload/', upload),
    path('upload_file/', upload_file),
    path('test01/',test01),
    path('object_detection/',object_detection),
]