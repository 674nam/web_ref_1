from django.contrib import admin
from .models import Member,Category,Post

admin.site.register(Member)

# 演習 ※投稿機能を作成する 追加
admin.site.register(Category)
admin.site.register(Post)
