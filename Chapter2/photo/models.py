from django.db import models

# Create your models here.

class Photo(models.Model): # models.Model을 상속받음
    title = models.CharField(max_length=50) # 각 속성을 models로 정의함
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()



    # CharField
    # IntegerField
    # TextField
    # DataField
    # DataTimeField
    # FileField
    # ImageField
    # ForeignKey
    # OneToOneField
    # ManyToManyField