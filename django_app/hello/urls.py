# p.61 helloフォルダ内にurls.pyを作成

# # リスト2-5 p.62, 2-15 p.80
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
# ]

# # リスト2-21 p.86
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("next", views.next, name = "next"),
# ]

# # リスト2-27 p.97
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("form", views.form, name = "form"),
# ]

# # リスト2-31 p.105
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
# ]

# # リスト2-36 p.113
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.IndexView.as_view(), name = "index"),
# ]

# # リスト3-11 p.188
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
# ]

# # リスト3-27 p.210
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("create", views.create, name = "create"),
# ]

# # リスト3-31 p.215
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("create", views.create, name = "create"),
#     path("edit/<int:num>", views.edit, name = "edit"),
# ]

# # リスト3-31 p.215
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("create", views.create, name = "create"),
#     path("edit/<int:num>", views.edit, name = "edit"),
#     path("delete/<int:num>", views.delete, name = "delete"),
# ]

# # リスト3-43 p.233
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("create", views.create, name = "create"),
#     path("edit/<int:num>", views.edit, name = "edit"),
#     path("delete/<int:num>", views.delete, name = "delete"),
#     path("find", views.find, name = "find"),
# ]

# # リスト4-10 p.276
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("create", views.create, name = "create"),
#     path("edit/<int:num>", views.edit, name = "edit"),
#     path("delete/<int:num>", views.delete, name = "delete"),
#     path("find", views.find, name = "find"),
#     path("check", views.check, name = "check"),
# ]

# # リスト4-30 p.308
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("create", views.create, name = "create"),
#     path("edit/<int:num>", views.edit, name = "edit"),
#     path("delete/<int:num>", views.delete, name = "delete"),
#     path("find", views.find, name = "find"),
#     path("check", views.check, name = "check"),
#     path("<int:num>", views.index, name = "index"),
# ]

# リスト4-36 p.332
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("create", views.create, name = "create"),
    path("edit/<int:num>", views.edit, name = "edit"),
    path("delete/<int:num>", views.delete, name = "delete"),
    path("find", views.find, name = "find"),
    path("check", views.check, name = "check"),
    path("<int:num>", views.index, name = "index"),
    path("message/", views.message, name = "message"),
    path("message/<int:page>", views.message, name = "message"),

]