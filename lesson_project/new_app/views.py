# □演習問題
# ○lesson_projectに新規アプリ、new_appを追加してください。
# ○new_appに以下の要件を満たすテーブルを作成してください。

# Memberテーブル
# ・username -文字型、最大文字数100文字
# ・phone -数値型
# ・age -数値型、最大値3桁←すみませんこれなしで。
# ・mail -文字型、emailfieldとする、最大文字数100文字

# ○テーブルにダミーレコードを10件以上追加し、以下のhtmlを作成してください。
# ・index.html -トップページ。レコード一覧の表示。
# ・post.html -投稿ページ。Memberテーブルにレコードを追加する。投稿後はindex.htmlに戻る。
# ・search.html -検索ページ。検索フォームを作成し、Memberテーブルのnameの列から一致するレコードを取り出す。

# ※関数名の指定はありません。コピペできるものは、どこであれ自由に使ってよいものとします。

# 演習
# lesson_projectに投稿機能を作成してください。
# 条件は以下の通りです。

# ■Categoryテーブル
# ・name
# ex)音楽のこと、ITのこと、ファッションのこと、など

# ■Postテーブル
# だれが、いつ、どのカテゴリーに、どんなことを投稿したのか、わかるように設計してください。

# 投稿機能の仕様は、皆さんが検討し、設計してください。
# 各テーブルにフォームを作るべきかどうかも検討して下さい。
# 結果として、Postテーブルのレコードが一覧表示されていればよいものとします。

# おまけ★★★★
# カテゴリーごとの絞り込み機能を実装してください。
# ・条件、index関数で絞り込み処理を行ってください。


# # 演習問題
# from django.shortcuts import render
# from django.shortcuts import redirect

# from .models import Member
# from .forms import MemberForm, SeachForm

# def index(request):
#     data = Member.objects.all()
#     params = {
#         "title":"new_app",
#         "data":data,
#     }
#     return render(request, "new_app/index.html", params)

# def post(request):
#     if (request.method == "POST"):
#         member = MemberForm(request.POST)
#         member.save()
#         return redirect(to = "/new_app")
#     params = {
#     "title":"new_app",
#     "form":MemberForm(),
#     }
#     return render(request, "new_app/post.html", params)

# def seach(request):
#     if (request.method == "POST"):
#         form = SeachForm(request.POST)
#         seach = request.POST["seach"]
#         data = Member.objects.filter(username__icontains = seach)
#         msg = f"Result: {str(data.count())}"
#     else:
#         msg = "seach words..."
#         form = SeachForm()
#         data = Member.objects.all()
#     params ={
#         "title":"new_app",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "new_app/seach.html", params)

# # 演習問題 ID,Age昇順降順
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Sum, Max

# from .models import Member
# from .forms import MemberForm, SeachForm, SortForm

# def index(request):
#     # プルダウンformの表示も保存 paramsを上部に持ってくるとエラーになるため、
#     # 関数fmを使用
#     fm = SortForm()
#     if (request.method == "POST"):
#         ch = request.POST["choice"]
#         # print(ch)
#         data = Member.objects.all().order_by(ch)
#         fm = SortForm(request.POST)
#     else:
#         data = Member.objects.all()

#     re1 = Member.objects.aggregate(Sum("age"))
#     re2 = Member.objects.aggregate(Max("age"))
#     msg = f"Sum:{str(re1["age__sum"])} \
#             <br>Max:{str(re2["age__max"])}"
#     params = {
#         "title":"new_app",
#         'message':msg,
#         "form":fm,
#         "data":data,
#     }
#     return render(request, "new_app/index.html", params)

# def post(request):
#     if (request.method == "POST"):
#         member = MemberForm(request.POST)
#         member.save()
#         return redirect(to = "/new_app")
#     params = {
#     "title":"new_app",
#     "form":MemberForm(),
#     }
#     return render(request, "new_app/post.html", params)

# def seach(request):
#     if (request.method == "POST"):
#         form = SeachForm(request.POST)
#         seach = request.POST["seach"]
#         data = Member.objects.filter(username__icontains = seach)
#         msg = f"Result: {str(data.count())}"
#     else:
#         msg = "seach words..."
#         form = SeachForm()
#         data = Member.objects.all()
#     params ={
#         "title":"new_app",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "new_app/seach.html", params)

# # 演習 ※投稿機能を作成する
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Sum, Max
# from django.core.paginator import Paginator

# from .models import Member,Post
# from .forms import MemberForm, SeachForm, SortForm, PostForm

# def index(request):
#     fm = SortForm()
#     if (request.method == "POST"):
#         ch = request.POST["choice"]
#         data = Member.objects.all().order_by(ch)
#         fm = SortForm(request.POST)
#     else:
#         data = Member.objects.all()

#     re1 = Member.objects.aggregate(Sum("age"))
#     re2 = Member.objects.aggregate(Max("age"))
#     msg = f"Sum:{str(re1["age__sum"])} \
#             <br>Max:{str(re2["age__max"])}"
#     params = {
#         "title":"new_app",
#         'message':msg,
#         "form":fm,
#         "data":data,
#     }
#     return render(request, "new_app/index.html", params)

# def post(request, page = 1):
#     if (request.method == "POST"):
#         form = PostForm(request.POST)
#         form.save()
#     data = Post.objects.all().reverse()
#     paginator = Paginator(data, 5)
#     params = {
#         'title': 'Post',
#         'form': PostForm(),
#         'data': paginator.get_page(page),
#     }
#     return render(request, 'new_app/post.html', params)

# def seach(request):
#     if (request.method == "POST"):
#         form = SeachForm(request.POST)
#         seach = request.POST["seach"]
#         data = Member.objects.filter(username__icontains = seach)
#         msg = f"Result: {str(data.count())}"
#     else:
#         msg = "seach words..."
#         form = SeachForm()
#         data = Member.objects.all()
#     params ={
#         "title":"new_app",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "new_app/seach.html", params)

# おまけ※カテゴリーごとの絞込み機能、index関数(Post関数？)で絞込処理
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum, Max
from django.core.paginator import Paginator

from .models import Member,Post
from .forms import MemberForm, SeachForm, SortForm, PostForm, FilterForm
def index(request):
    fm = SortForm()
    if (request.method == "POST"):
        ch = request.POST["choice"]
        data = Member.objects.all().order_by(ch)
        fm = SortForm(request.POST)
    else:
        data = Member.objects.all()

    re1 = Member.objects.aggregate(Sum("age"))
    re2 = Member.objects.aggregate(Max("age"))
    msg = f"Sum:{str(re1["age__sum"])} \
            <br>Max:{str(re2["age__max"])}"
    params = {
        "title":"new_app",
        'message':msg,
        "form":fm,
        "data":data,
    }
    return render(request, "new_app/index.html", params)

def post(request, page = 1):
    if (request.method == "POST"):
        form = PostForm(request.POST)
        form.save()
    data = Post.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Post',
        'form': PostForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'new_app/post.html', params)

# def post_form(request):
#     if (request.method == "POST"):
#         form = PostForm(request.POST)
#         form.save()
#         return redirect(to = "/post_list")
#     params = {
#     "title":"post_form",
#     "form":PostForm(),
#     }
#     return render(request, "new_app/post_form.html", params)

def seach(request):
    if (request.method == "POST"):
        form = SeachForm(request.POST)
        seach = request.POST["seach"]
        data = Member.objects.filter(username__icontains = seach)
        msg = f"Result: {str(data.count())}"
    else:
        msg = "seach words..."
        form = SeachForm()
        data = Member.objects.all()
    params ={
        "title":"new_app",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "new_app/seach.html", params)