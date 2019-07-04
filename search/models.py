from django.db import models
import os
from django.core.files import File
# Create your models here.

class Files(models.Model):
    
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files')


def save_file(name, f):
	#метод для сохранения файла
	#Сначала записываем файл во временную дерикторию tmp
    destination = open('/tmp/'+ name , 'wb+') 
    for chunk in f.chunks():
        destination.write(chunk)
    #После этого создаем нувую запись в БД
    django_file = File(destination)
    f = Files()
    f.name = name
    f.file.save(name, django_file, save=True)
    destination.close()
    django_file.close()
    #удаляем файл из временной дериктории
    os.remove('/tmp/'+name)
