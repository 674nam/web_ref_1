from django.urls import path
from . import views

app_name = 'money'
urlpatterns = [
        path('', views.index, name='index'), #views.indexはあとで作る
        path('<int:year>/<int:month>', views.index, name='index'), # 追加
        ]