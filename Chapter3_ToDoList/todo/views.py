from django.shortcuts import render, redirect
from .models import Todo 
from .forms import TodoForm

def todo_list(request): # 요청을 받아 함수를 실행한다
    todos = Todo.objects.filter(complete=False) # 클래스 내에 complete가 거짓 일 경우에만 todos에 데이터를 넘겨준다. 또 filter 함수는 여러개의 객체를 가져온다.
    return render(request, 'todo/todo_list.html', {'todos': todos}) # 오른쪽에 있는 todos를 왼쪽에 'todos'(html에 들어갈) 에 대입해준다todo_list.html을 랜더링 한다.

def todo_detail(request, pk): # 요청과 pk 값을 받아 함수를 실행한다.
    todo =  Todo.objects.get(id=pk)  # id와 pk가 일치하면 Todo에 단일한 인스턴스를 불러와 todo에 저장한다.
    # return render(request, 'todo/todo_detail.html', {'todo': todo})
    return render(request, 'todo/todo_detail.html', {'todo': todo}) # 오른쪽에 있는 todo를 왼쪽에 'todo'(html에 들어갈) 에 대입해준다todo_detail.html을 랜더링 한다.

def todo_post(request): # 요청을 받아 함수를 실행한다
    if request.method == 'POST': # 만약 request의 메소드가 post면
        form = TodoForm(request.POST) # 요청이 post라면 TodoForm에 작성한 데이터로 form이라는 새로운 인스턴스를 생성한다.
        if form.is_valid(): # 만약 작성된 form이 유효하다면
            todo = form.save(commit=False) # form에서 제출된 데이터를 기반으로 todo라는 클래스를 임시로 생성한다
            todo.save() # todo를 저장한다
            return redirect('todo_list') # todo_list url로 이동한다
    else: # 만약 request의 메소드가 post가 아니라면
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form}) # 'form'(html에 사용할 변수)에 form을 대입하고 todo_post.html를 반환한다


def todo_edit(request, pk): # 요청과 pk 값을 받아 함수를 실행한다.
    todo = Todo.objects.get(id=pk) # id와 pk가 일치하면 Todo에 단일한 인스턴스를 불러와 todo에 저장한다. (수정하기 위한 객체를 가져온다)
    if request.method == 'POST': # 만약 request의 메소드가 post면
        form = TodoForm(request.POST, instance=todo) #  이해가 안된다
        if form.is_valid(): # 만약 작성된 form이 유효하다면
            todo = form.save(commit=False) # form에서 제출된 데이터를 기반으로 todo라는 클래스를 임시로 생성한다
            todo.save() # 임시로 생성된 todo를 저장한다
            return redirect('todo_list') # todo_list url로 이동한다
    else: # 만약 request의 메소드가 post가 아니라면
        form = TodoForm(instance=todo) # 이해가 안된다.
    # return render(request, 'todo/todo_post.html', {'form', form}) # 실수한 부분
    return render(request, 'todo/todo_post.html', {'form': form}) # 'form'(html에 사용할 변수)에 form을 대입하고 todo_post.html를 반환한다


def done_list(request): # 요청을 받아 함수를 실행한다
    dones = Todo.objects.filter(complete=True) # complete가 True인 클래스들을 모두 가져와서 dones에 대입한다.  
    return render(request, 'todo/done_list.html', {'dones': dones}) # 'dones'(html에 사용할 변수)에 dones을 대입하고 done_list.html를 반환한다


def todo_done(request, pk): # 요청과 pk 값을 받아 함수를 실행한다.
    todo = Todo.objects.get(id=pk) # id와 pk가 일치하면 Todo에 단일한 인스턴스를 불러와 todo에 저장한다.
    todo.complete = True # todo에 complete 필드를 true로 설정한다.
    todo.save() # todo를 저장한다.
    return redirect('todo_list') # todo_list url로 이동한다


# Create your views here.
