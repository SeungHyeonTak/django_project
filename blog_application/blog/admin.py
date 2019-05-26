from django.contrib import admin
from .models import Blog

# models.py에서 셋팅했던것들을 받아옴
admin.site.register(Blog)