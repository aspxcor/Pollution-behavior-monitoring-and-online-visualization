from django.db import models

'''
python manage.py makemigrations
python manage.py migrate
'''

# }#


# class Car(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     photo = models.ImageField(upload_to='cars')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
class  peolple_origin(models.Model):
    origin_province =  models.CharField(max_length=20,verbose_name='省份名称')
    people_count = models.IntegerField(verbose_name='省份数量')
class crime_analyze(models.Model):
    type_name = models.CharField(max_length=20,verbose_name='类型名称')
    type_value = models.IntegerField(verbose_name='类型数量')
class age_distribution(models.Model):
    age_distribution_type = models.CharField(max_length=20,verbose_name='年龄段')
    age_distribution_value = models.IntegerField(verbose_name='年龄段内人数')
class time_line_statistics(models.Model):
    time_line_statistics_type = models.CharField(max_length=20,verbose_name='时间段')
    time_line_statistics_value = models.IntegerField(verbose_name='时间段内人数')