# リスト5-3 p.357
from django.contrib import admin
from .models import Message, Good

admin.site.register(Message)
admin.site.register(Good)