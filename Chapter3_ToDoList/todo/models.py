from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100) # 제목 입력란(최대 100자)
    description = models.TextField(blank=True) # todo에 대한 설명
    created = models.DateTimeField(auto_now_add=True) # 생성일자
    complete = models.BooleanField(default=False) # 완료여부
    important = models.BooleanField(default=False) # 중요여부

    def __str__(self):
        return self.title