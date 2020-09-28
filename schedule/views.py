from django.shortcuts import render
from django.shortcuts import redirect
from .form import postSchedule, signupCategory
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
    today = datetime.datetime.now()
    nowYear = int(today.strftime('%Y'))
    nowMonth = int(today.strftime('%m'))
    nowDay = int(today.strftime('%d'))

    try:
        year = int(requestDate['year'][0])
        month = int(requestDate['month'][0])
    except KeyError:
        year = nowYear
        month = nowMonth
    firstDay = datetime.datetime(year,month,1,0,0,0)
    nextMonth = month + 1
    nextDate = datetime.datetime(nowYear, nextMonth, 1, 23, 59, 59)
    lastDay = nextDate - timedelta(days=1)
    lastDays = int(lastDay.strftime('%d'))
    post = Sche.objects.filter(scheduleOwner=request.user).filter(startDate__gte= datetime.datetime(year,month,1,0,0,0)).filter(lastDate__lte=datetime.datetime(year,month,lastDays,23,59,59))
    return render(request, 'index.html', {'post': post, 'nowYear': nowYear, 'nowMonth': nowMonth, 'nowDay': nowDay, 'firstDay': firstDay})

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
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
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
def schedule(request):
    today = datetime.datetime.now()
    nowYear = int(today.strftime('%Y'))
    nowMonth = int(today.strftime('%m'))
    nowDay = int(today.strftime('%d'))
    if request.method == 'POST' and request.user.id:
        form = postSchedule(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.scheduleOwner_id = request.user.id
            post.save()
            return redirect('index')
    else:
        form = postSchedule()
        return render(request, 'schedule.html', {'form': form, 'nowYear': nowYear, 'nowMonth': nowMonth, 'nowDay': nowDay})

def category(request):
    if request.method == "POST" and request.user.id:
        form = signupCategory(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.categoryOwner_id = request.user.id
            post.save()
            return redirect('index')
    else:
        form = signupCategory()
        return render(request, 'category.html', {'form': form})