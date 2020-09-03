from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    categoryName = models.CharField(max_length=10)
    categoryOwner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.categoryName)
    class Meta:
        verbose_name_plural = "카테고리"

class schedule(models.Model):
    startDate = models.DateTimeField()
    lastDate = models.DateTimeField()
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    categoryNum = models.ForeignKey(category, on_delete=models.CASCADE)
    scheduleOwner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "일정"
