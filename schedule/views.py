from django.shortcuts import render
from django.shortcuts import redirect
from .form import postSchedule
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def index(request):
    return render(request, 'index.html')

def schedule(request):
    if request.method == 'POST':
        form = postSchedule(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.scheduleOwner = request.user.id
            form.save()


    form = postSchedule()

    return render(request, 'schedule.html', {'form': form})

def signup(request):
    # HTTP Method가 POST 인 경우
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
    # 모델폼의 유효성 검증이 valid할 경우, DB에 저장
        if signup_form.is_valid():
            signup_form.save()
        return redirect('/')

# HTTP Method가 GET 인 경우
    else:
        signup_form = UserCreationForm()

    return render(request, 'signup.html', {'signup_form': signup_form})


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('/')

    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})