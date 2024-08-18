from django import forms
from .models import Photo # model에서 Photo class 상속

class PhotoForm(forms.ModelForm): # forms.ModelsForm을 상속
    class Meta:
        model = Photo
        fields = (      # ModelForm을 상속받아 아래의 필드값 작성
            'title',
            'author',
            'image',
            'description',
            'price',
        )