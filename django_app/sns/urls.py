# # リスト5-5 p.364
# from django.urls import path
# from .import views

# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("<int:page>", views.index, name = "index"),
#     path("post", views.post, name = "post"),
#     path("goods", views.goods, name = "goods"),
#     path("good/<int:good_id>", views.good, name = "good"),
# ]

# # 演習①
# # django_appのsnsアプリケーションに以下の機能を追加してください。
# # ・投稿内容編集機能
# # ・投稿削除機能
# # 仕様は問いませんが、それぞれでhtml、ルーティング、view関数を作成するのがやりやすいと思います。
# from django.urls import path
# from .import views

# urlpatterns = [
#     path("", views.index, name = "index"),
#     path("<int:page>", views.index, name = "index"),
#     path("post", views.post, name = "post"),
#     path("goods", views.goods, name = "goods"),
#     path("good/<int:good_id>", views.good, name = "good"),
#     path("edit/<int:edit_id>", views.edit, name = "edit"),
#     path("delete/<int:delete_id>", views.delete, name = "delete"),
# ]

# 演習③←new!
# ・投稿一覧からユーザー名をクリックすると、投稿の絞り込みができる
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:page>", views.index, name = "index"),
    path("post", views.post, name = "post"),
    path("goods", views.goods, name = "goods"),
    path("good/<int:good_id>", views.good, name = "good"),
    path("edit/<int:edit_id>", views.edit, name = "edit"),
    path("delete/<int:delete_id>", views.delete, name = "delete"),
    path("find/<int:find_id>", views.find, name = "find"),
]