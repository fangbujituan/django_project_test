# 在这里注册您的模型。
from django.contrib import admin
from .models import Comment

admin.site.register(Comment)