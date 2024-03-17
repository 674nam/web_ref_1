# # 課題1,2
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# 課題3
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
]

# 好きなように仕様変更してみる
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    # path('', views.form, name=''),不要
    # path('', views.form, name='back'),不要
]