# # 演習問題
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('post', views.post, name='post'),
#     path('seach', views.seach, name='seach'),
# ]

# # 演習 ※投稿機能を作成する
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('seach', views.seach, name='seach'),
#     path('post/', views.post, name='post'),
#     path('post/<int:page>', views.post, name='post'),
# ]

# おまけ※カテゴリーごとの絞込み機能、index関数(Post関数？)で絞込処理
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seach', views.seach, name='seach'),
    path('post/', views.post, name='post'),
    path('post/<int:page>', views.post, name='post'),
    # path('post_form', views.post_form, name='post'),
]