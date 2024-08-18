from django.shortcuts import render, get_object_or_404, redirect # django.shortcuts라는 패키지에서 다양한 함수를 가져옴
from .models import Photo # models.py에서 Photo라는 클래스를 가져옴
from .forms import PhotoForm # forms.py에서 PhotoForm이라는 클래스를 가져옴


def photo_list(request):
    return render(request, 'photo/photo_list.html', {}) # photo_list.html를 랜더링하는 함수 호출


def photo_list_two(request):
    photos = Photo.objects.all() # photos라는 변수에 Photo에 있는 모든 인스턴스를 대입
    return render(request, 'photo/photo_list_two.html', {'photos': photos}) # photo_list.html를 랜더링하는 함수 호출


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk) # photo의 객체를 가져오거나 404 오류를 보여준
    return render(request, 'photo/photo_detail.html', {'photo': photo}) # photo_list.html를 랜더링하는 함수 호출


def photo_post(request): 
    if request.method == "POST": # 만약 form의 method가 post라면
        form = PhotoForm(request.POST) # form이라는 변수에 PhotoForm 클래스에 있는 인스턴스를 대입
        if form.is_valid(): # 만약 form의 데이터가 유효하다면 
            photo = form.save(commit=False) # save(commit=False) 이것의 기능을 잘 모르겠음
            photo.save() # valid 함수로 데이터가 유효한 것을 확인하면 photo에서 받아온 데이터를 받아 저장한다
            return redirect('photo_detail', pk=photo.pk) # 새로 저장된 photo의 pk의 세부 페이지를 반환
    else: # post 요청이 아니라면
        form = PhotoForm() # ???
    return render(request, 'photo/photo_post.html', {'form': form})


def photo_edit(request, pk): # 내일 urls랑 photo_detail.html 작성 70페이지부터 시작
    photo = get_object_or_404(Photo, pk=pk) # Photo의 인스턴스를 가져오거나 404 HTTP 코드를 반환한다.
    if request.method == "POST": # 만약 form의 요청이 post면
        form = PhotoForm(request.POST, instance=photo) # form이라는 변수에 요청한 PhotoForm의 인스턴스를 대입한다
        if form.is_valid(): # 만약 데이터를 검사했을 때 유효하면
            photo = form.save(commit=False) 
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form': form})





# Create your views here.
# https://github.com/TaeBbong/drf_for_backend/blob/master/02_%EC%82%AC%EC%A7%84%EB%AA%A9%EB%A1%9D/photo/templates/photo/photo_list.html
# pk와 fk의 개념