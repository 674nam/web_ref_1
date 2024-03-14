# 課題1
# P.108までのコピーアプリを作成してください。
# ただし、作成するプロジェクト名とアプリ名は以下で統一してください。
# プロジェクト名 :lesson_project
# アプリ名		 :lesson_app

# 課題2
# 作成したコピーアプリに以下の仕様を追加してください。
# ・ラジオボタンを含んだフォームの作成。
# ・フォームで送信した情報を画面に表示。
# ※テキストP.130のリスト2-49を参考にしてください。
# ただし、viewは関数ベースビューに書き直してください。

# 課題3
# フォームで送信した際に別のhtmlページが呼び出されるように仕様変更してください。

# # 課題2
# from django.shortcuts import render
# from .forms import HelloForm

# def index(request):
#     params = {
#     'title': 'Hello',
#     'form': HelloForm(),
#     'result': None,
#     }
#     if (request.method == 'POST'):
#         ch = request.POST['choice']
#         params['result'] = 'selected: "' + ch + '".'
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'lesson_app/index.html', params)

# # 課題3
# from django.shortcuts import render
# from .forms import HelloForm

# def index(request):
#     params = {
#     'title': 'Hello',
#     'form': HelloForm(),
#     'result': None,
#     }
#     return render(request, 'lesson_app/index.html', params)

# def form(request):
#     params = {
#     'title':'Hello/Form',
#     'form': HelloForm(),
#     'result': None,
#     }
#     if (request.method == 'POST'):
#         ch = request.POST['choice']
#         params['result'] = 'selected: "' + ch + '".'
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'lesson_app/index.html', params)

# 好きなように仕様変更してみる
from django.shortcuts import render
from .forms import HelloForm

def index(request):
    params = {
    'title': 'Hello',
    'form': HelloForm(),
    'result': None,
    'goto': '',
    }
    return render(request, 'lesson_app/index.html', params)

def form(request):
    params = {
    'title':'Hello/Form',
    'form': HelloForm(),
    'result': None,
    'goto': 'back',
    }
    if (request.method == 'POST'):
        ch = request.POST['choice']
        # print(ch)
        params['result'] = 'selected: "' + ch + '".'
        params['form'] = HelloForm(request.POST)
        # print('SSSSSSSSS')
    return render(request, 'lesson_app/index.html', params)