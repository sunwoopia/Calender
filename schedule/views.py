from django.shortcuts import render
from django.shortcuts import redirect
from .form import postSchedule
from .form import UserForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import schedule as Sche
import datetime
from datetime import timedelta

from urllib.parse import parse_qs

def index(request):
    requestDate = parse_qs(request.META['QUERY_STRING'])
    print(requestDate['year'][0])
    print(requestDate['month'][0])
    today = datetime.datetime.now()
    nowYear = int(today.strftime('%Y'))
    nowMonth = int(today.strftime('%m'))
    nextMonth = nowMonth + 1
    nextDate = datetime.datetime(nowYear, nextMonth, 1, 23, 59, 59)
    lastDay = nextDate - timedelta(days=1)
    lastDays = int(lastDay.strftime('%d'))
    post = Sche.objects.filter(scheduleOwner=request.user).filter(startDate__gte= datetime.datetime(nowYear,nowMonth,1,0,0,0)).filter(lastDate__lte=datetime.datetime(nowYear,nowMonth,lastDays,23,59,59))
    return render(request, 'index.html', {'post': post})


def schedule(request):
    if request.method == 'POST' and request.user.id:
        form = postSchedule(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.scheduleOwner_id = request.user.id
            post.save()
            return redirect('index')
    else:
        form = postSchedule()
        return render(request, 'schedule.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
def signin(request):
    if request.Pmethod == "POST":
        form = LoginForm(request.POST)
        username = request.OST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


# def get_name(request):
#     name = User.objects.order_by('name')
#     context = {'name': name}
#     return render(request, 'index.html', name)
# def signup(request):
#     # HTTP Method가 POST 인 경우
#     if request.method == 'POST':
#         signup_form = UserCreationForm(request.POST)
#     # 모델폼의 유효성 검증이 valid할 경우, DB에 저장
#         if signup_form.is_valid():
#             signup_form.save()
#         return redirect('/')
#
# # HTTP Method가 GET 인 경우
#     else:
#         signup_form = UserCreationForm()
#
#     return render(request, 'signup.html', {'signup_form': signup_form})


# def login(request):
#     if request.method == 'POST':
#         login_form = AuthenticationForm(request, request.POST)
#         if login_form.is_valid():
#             auth_login(request, login_form.get_user())
#         return redirect('/')
#
#     else:
#         login_form = AuthenticationForm()
#
#     return render(request, 'login.html', {'login_form': login_form})