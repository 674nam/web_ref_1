# # リスト5-7 p.365
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required

# from .models import Message, Good
# from .forms import MessageForm

# @login_required(login_url = "/admin/login/")
# def index(request, page = 1):
#     max = 10
#     form = MessageForm() # ()内 request.user 削除
#     msgs = Message.objects.all()
#     paginate = Paginator(msgs, max)
#     page_items = paginate.get_page(page)

#     params = {
#         "login_user":request.user,
#         "form": form,
#         "contents":page_items,
#     }
#     return render(request, "sns/index.html", params)

# @login_required(login_url = "/admin/login/")
# def goods(request):
#     goods = Good.objects.filter(owner = request.user).all()
#     params = {
#         "login_user":request.user,
#         "contents":goods,
#     }
#     return render(request, "sns/good.html", params)

# @login_required(login_url = "/admin/login/")
# def post(request):
#     if request.method == "POST":
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit = False)
#             post.owner = request.user
#             post.save()
#             return redirect(to = "/sns/")
#     else:
#         messages = Message.objects.filter(owner = request.user).all()
#         params = {
#             "login_user":request.user,
#             "contents":messages,
#         }
#         return render(request, "sns/post.html", params)

# @login_required(login_url = "/admin/login/")
# def good(request, good_id):
#     good_msg = Message.objects.get(id = good_id)
#     is_good = Good.objects.filter(owner = request.user)\
#         .filter(message = good_msg).count()
#     if is_good > 0:
#         messages.success(request, "既にメッセージにはGoodしています。")
#         return redirect(to = "/sns")

#     good_msg.good_count += 1
#     good_msg.save()
#     good = Good()
#     good.owner = request.user
#     good.message = good_msg
#     good.save()
#     messages.success(request, "メッセージにGoodしました!")
#     return redirect(to = "/sns")

# 演習①
# django_appのsnsアプリケーションに以下の機能を追加してください。
# ・投稿内容編集機能
# ・投稿削除機能
# 仕様は問いませんが、それぞれでhtml、ルーティング、view関数を作成するのがやりやすいと思います。
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required

# from .models import Message, Good
# from .forms import MessageForm

# @login_required(login_url = "/admin/login/")
# def index(request, page = 1):
#     max = 10
#     form = MessageForm() # ()内 request.user 削除
#     msgs = Message.objects.all()
#     paginate = Paginator(msgs, max)
#     page_items = paginate.get_page(page)

#     params = {
#         "login_user":request.user,
#         "form": form,
#         "contents":page_items,
#     }
#     return render(request, "sns/index.html", params)

# @login_required(login_url = "/admin/login/")
# def goods(request):
#     goods = Good.objects.filter(owner = request.user).all()
#     params = {
#         "login_user":request.user,
#         "contents":goods,
#     }
#     return render(request, "sns/good.html", params)

# @login_required(login_url = "/admin/login/")
# def post(request):
#     if request.method == "POST":
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit = False)
#             post.owner = request.user
#             post.save()
#             return redirect(to = "/sns/")
#     else:
#         messages = Message.objects.filter(owner = request.user).all()
#         params = {
#             "login_user":request.user,
#             "contents":messages,
#         }
#         return render(request, "sns/post.html", params)

# @login_required(login_url = "/admin/login/")
# def good(request, good_id):
#     good_msg = Message.objects.get(id = good_id)
#     is_good = Good.objects.filter(owner = request.user)\
#         .filter(message = good_msg).count()
#     if is_good > 0:
#         messages.success(request, "既にメッセージにはGoodしています。")
#         return redirect(to = "/sns")

#     good_msg.good_count += 1
#     good_msg.save()
#     good = Good()
#     good.owner = request.user
#     good.message = good_msg
#     good.save()
#     messages.success(request, "メッセージにGoodしました!")
#     return redirect(to = "/sns")

# @login_required(login_url = "/admin/login/")
# def edit(request, edit_id):
#     edit_msg = Message.objects.get(id = edit_id)
#     if (request.method == "POST"):
#         edit = MessageForm(request.POST, instance = edit_msg)
#         edit.save()
#         return redirect(to = "/sns")
#     params = {
#         "title":"Edit",
#         "id":edit_id,
#         "form":MessageForm(instance = edit_msg),
#     }
#     return render(request, "sns/edit.html", params)

# @login_required(login_url = "/admin/login/")
# def delete(request, delete_id):
#     delete_msg = Message.objects.get(id = delete_id)
#     if (request.method == "POST"):
#         delete_msg.delete()
#         return redirect(to = "/sns")
#     params = {
#         "title":"delete",
#         "id":delete_id,
#         "obj":delete_msg,
#     }
#     return render(request, "sns/delete.html", params)

# # 演習②
# # django_appのsnsアプリケーションを以下の仕様に変更してください。
# # ・good済みの投稿に、再度goodをすると、goodが解除される
# # ・解除されたら画面に「goodが解除されました」とシステムメッセージを表示する
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required

# from .models import Message, Good
# from .forms import MessageForm

# @login_required(login_url = "/admin/login/")
# def index(request, page = 1):
#     max = 10
#     form = MessageForm()
#     msgs = Message.objects.all()
#     paginate = Paginator(msgs, max)
#     page_items = paginate.get_page(page)

#     params = {
#         "login_user":request.user,
#         "form": form,
#         "contents":page_items,
#     }
#     return render(request, "sns/index.html", params)

# @login_required(login_url = "/admin/login/")
# def goods(request):
#     goods = Good.objects.filter(owner = request.user).all()
#     params = {
#         "login_user":request.user,
#         "contents":goods,
#     }
#     return render(request, "sns/good.html", params)

# @login_required(login_url = "/admin/login/")
# def post(request):
#     if request.method == "POST":
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit = False)
#             post.owner = request.user
#             post.save()
#             return redirect(to = "/sns/")
#     else:
#         messages = Message.objects.filter(owner = request.user).all()
#         params = {
#             "login_user":request.user,
#             "contents":messages,
#         }
#         return render(request, "sns/post.html", params)

# @login_required(login_url = "/admin/login/")
# def good(request, good_id):
#     good_msg = Message.objects.get(id = good_id)
#     my_good = Good.objects.filter(owner = request.user)\
#         .filter(message = good_msg)
#     is_good = my_good.count()
#     if is_good > 0:
#         messages.success(request, "既にメッセージにはGoodしています。")
#         messages.success(request, "goodが解除されました")
#         good_msg.good_count -= 1
#         good_msg.save()
#         my_good.delete()
#         return redirect(to = "/sns")

#     good_msg.good_count += 1
#     good_msg.save()
#     good = Good()
#     good.owner = request.user
#     good.message = good_msg
#     good.save()
#     messages.success(request, "メッセージにGoodしました!")
#     return redirect(to = "/sns")

# @login_required(login_url = "/admin/login/")
# def edit(request, edit_id):
#     edit_msg = Message.objects.get(id = edit_id)
#     if (request.method == "POST"):
#         edit = MessageForm(request.POST, instance = edit_msg)
#         edit.save()
#         return redirect(to = "/sns")
#     params = {
#         "title":"Edit",
#         "id":edit_id,
#         "form":MessageForm(instance = edit_msg),
#     }
#     return render(request, "sns/edit.html", params)

# @login_required(login_url = "/admin/login/")
# def delete(request, delete_id):
#     delete_msg = Message.objects.get(id = delete_id)
#     if (request.method == "POST"):
#         delete_msg.delete()
#         return redirect(to = "/sns")
#     params = {
#         "title":"delete",
#         "id":delete_id,
#         "obj":delete_msg,
#     }
#     return render(request, "sns/delete.html", params)

# 演習③←new!
# ・投稿一覧からユーザー名をクリックすると、投稿の絞り込みができる
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Message, Good
from .forms import MessageForm

@login_required(login_url = "/admin/login/")
def index(request, page = 1):
    max = 10
    form = MessageForm()
    msgs = Message.objects.all()
    paginate = Paginator(msgs, max)
    page_items = paginate.get_page(page)

    params = {
        "login_user":request.user, # layout.htmlで指定
        "form": form,
        "contents":page_items,
    }
    return render(request, "sns/index.html", params)

@login_required(login_url = "/admin/login/")
def goods(request):
    goods = Good.objects.filter(owner = request.user).all()
    params = {
        "login_user":request.user, # layout.htmlで指定
        "contents":goods,
    }
    return render(request, "sns/good.html", params)

@login_required(login_url = "/admin/login/")
def post(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.owner = request.user
            post.save()
            return redirect(to = "/sns/")
    else:
        messages = Message.objects.filter(owner = request.user).all()
        params = {
            "login_user":request.user, # layout.htmlで指定
            "contents":messages,
        }
        return render(request, "sns/post.html", params)

@login_required(login_url = "/admin/login/")
def good(request, good_id):
    good_msg = Message.objects.get(id = good_id)
    my_good = Good.objects.filter(owner = request.user)\
        .filter(message = good_msg)
    is_good = my_good.count()
    if is_good > 0:
        messages.success(request, "既にメッセージにはGoodしています。")
        messages.success(request, "goodが解除されました")
        good_msg.good_count -= 1
        good_msg.save() # カウント数の保存
        my_good.delete() # テーブルからGoodレコードを削除
        return redirect(to = "/sns")

    good_msg.good_count += 1
    good_msg.save() # カウント数の保存
    good = Good() # テーブルへGoodレコードを追加
    good.owner = request.user # テーブルへGoodレコードを追加
    good.message = good_msg # テーブルへGoodレコードを追加
    good.save() # テーブルへGoodレコードを追加
    messages.success(request, "メッセージにGoodしました!")
    return redirect(to = "/sns")

@login_required(login_url = "/admin/login/")
def edit(request, edit_id):
    edit_msg = Message.objects.get(id = edit_id) # index.htmlのitem.id⇒edit_idレコード1つ取り出し
    if (request.method == "POST"):
        edit = MessageForm(request.POST, instance = edit_msg)
        edit.save()
        return redirect(to = "/sns")
    params = {
        "login_user":request.user, # layout.htmlで指定
        # "title":"edit", # htmlに{% block title %}{{title}}{% endblock %}記述があるとき
        "id":edit_id,
        "form":MessageForm(instance = edit_msg),
    }
    return render(request, "sns/edit.html", params)

@login_required(login_url = "/admin/login/")
def delete(request, delete_id):
    delete_msg = Message.objects.get(id = delete_id) # index.htmlのitem.id⇒delete_idレコード1つ取り出し
    if (request.method == "POST"):
        delete_msg.delete()
        return redirect(to = "/sns")
    params = {
        "login_user":request.user, # layout.htmlで指定
        # "title":"delete", # htmlに{% block title %}{{title}}{% endblock %}記述があるとき
        "id":delete_id,
        "obj":delete_msg,
    }
    return render(request, "sns/delete.html", params)

@login_required(login_url = "/admin/login/")
def find(request, find_id):
    find_msg = Message.objects.get(id = find_id) # index.htmlのitem.id⇒find_idレコード1つ取り出し
    # print(find_msg)  # クリックした投稿 プリントデバッグ用
    # print(find_msg.owner.id,"DFFFFFFFFFFFFFFFF") # プリントデバッグ用
    # print(find_msg.owner,"DFFFFFFFFFFFFFFFF")    # プリントデバッグ用
    # find_user = find_msg.owner.id # 取り出したレコード(インスタンス)ownerのid（Messageテーブル）取得
    find_user = find_msg.owner # 取り出したレコードのowner名を取得
    find_post = Message.objects.filter(owner = find_user).all # ownerの投稿を絞り込み検索。

    params = {
        "login_user":request.user, # layout.htmlで指定
        # "title":"find", # htmlに{% block title %}{{title}}{% endblock %}記述があるとき
        "message":f"{find_msg.owner}の投稿一覧",
        "contents":find_post,
    }
    return render(request, "sns/find.html", params)


