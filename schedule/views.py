from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .form import postSchedule
from .models import schedule

def index(request):
    return render(request, 'index.html')

def schedule(request):
    if request.method == 'POST':
        form = postSchedule(request.POST)
        print("데이터가 넘어옴")
        if form.is_valid():
            post = form.save(commit=False)
            # post.scheduleOwner = request.user.id
            print("값 검증 성공")
            form.save()


    form = postSchedule()

    return render(request, 'schedule.html', {'form': form})
