# from django.contrib import admin

# Register your models here.

# # リスト3-8 p.171
# from django.contrib import admin
# from .models import Friend

# admin.site.register(Friend)

# リスト4-35 p.329
from django.contrib import admin
from .models import Friend, Message

admin.site.register(Friend)
admin.site.register(Message)