from django.db import models

# Create your models here.

class Deal(models.Model):
    image_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, primary_key=True) #링크를 검사하면 중복되는 값이 있으면 제외하고(업데이트) 넘어감 
    reply_count = models.IntegerField()
    up_count = models.IntegerField()
