from django.contrib import admin
from .models import schedule
from .models import category

admin.site.register(schedule)
admin.site.register(category)