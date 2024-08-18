from django.urls import path # django.urls 라는 패키지에서 path라는 함수 호출
from . import views # views.py 호출


urlpatterns = [
    path('', views.photo_list, name='photo_list'), # 해당 url로 이동시 views에서 photo_list라는 함수를 호출
    path('second/', views.photo_list_two, name='photo_list_two'), # 해당 url로 이동시 views에서 photo_list_two라는 함수를 호출
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'), # 해당 url로 이동시 views에서 photo_detail라는 함수를 호출
    path('photo/new/', views.photo_post, name='photo_post'), # 해당 url로 이동시 views에서 photo_post라는 함수를 호출
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'), # 해당 url로 이동시 views에서 photo_edit라는 함수를 호출
]
