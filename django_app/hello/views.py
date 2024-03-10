# from django.shortcuts import render

# Create your views here.

# # リスト2-2 p.56
# from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, Django!!!")

# # リスト2-7 p.65
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     msg = request.GET["msg"]
#     return HttpResponse('you typed:"' + msg + '".')

# # リスト2-16 p.80
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request, "hello/index.html")

# # リスト2-18 p.83
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     params ={
#         "title":"Hello/Index",
#         "msg":"これはサンプルで作ったページです。",
#     }
#     return render(request, "hello/index.html", params)

# # リスト2-20 p.85
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     params ={
#         "title":"Hello/Index",
#         "msg":"これはサンプルで作ったページです。",
#         "goto":"next",
#     }
#     return render(request, "hello/index.html", params)

# def next(request):
#     params ={
#         "title":"Hello/Next",
#         "msg":"これは、もう１つのページです。",
#         "goto":"index",
#     }
#     return render(request, "hello/index.html", params)

# # リスト2-26 p.96
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     params ={
#         "title":"Hello/Index",
#         "msg":"お名前は？",
#     }
#     return render(request, "hello/index.html", params)

# def form(request):
#     msg = request.POST['msg']
#     params ={
#         "title":"Hello/Form",
#         "msg":f"こんにちは、{msg}さん。",
#     }
#     return render(request, "hello/index.html", params)

# # リスト2-29 p.101
# from django.shortcuts import render
# from .forms import HelloForm

# def index(request):
#     params ={
#         "title":"Hello",
#         "message":"your data:",
#         "form":HelloForm()
#     }
#     if (request.method == "POST"):
#         params["message"] = f"名前:{request.POST["name"]}\
#             <br>メール:{request.POST["mail"]}\
#             <br>年齢:{request.POST["age"]}"
#         params["form"] = HelloForm(request.POST)
#     return render(request, "hello/index.html", params)

# # リスト2-35 p.112
# # ⇒ Googleドライブ講義補足のソースコードへ変更
# from django.shortcuts import render
# from .forms import HelloForm
# from django.views.generic import FormView

# class IndexView(FormView):
#     template_name = 'hello/index.html'
#     form_class = HelloForm
#     success_url = '/'

#     def __init__(self):
#         self.params = {
#             'title':'Hello',
#             'message':'your data:',
#             'form':self.form_class(),
#         }

#     def get(self, request):
#         return render(self.request, self.template_name, self.params)

#     def form_valid(self, form):
#         self.params["message"] = '名前：{}<br>メール：{}<br>年齢：{}'.format(
#             form.cleaned_data['name'],
#             form.cleaned_data['mail'],
#             form.cleaned_data['age'],
#         )
#         print(self.request.POST)
#         self.params['form'] = self.form_class(self.request.POST)
#         return render(self.request, self.template_name, self.params)

# # リスト3-9 p.184
# from django.shortcuts import render
# from .models import Friend

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"hello",
#         "message":"all friends.",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# # リスト3-14 p.191
# from django.shortcuts import render
# from .models import Friend
# from .forms import HelloForm

# def index(request):
#     params = {
#         "title":"Hello",
#         "message":"all friends.",
#         "form":HelloForm(),
#         "data":[],
#     }
#     if (request.method == "POST"):
#         num = request.POST["id"]
#         item = Friend.objects.get(id = num)
#         params["data"] = [item]
#         params["form"] = HelloForm(request.POST)
#     else:
#         params["data"] = Friend.objects.all()
#     return render(request, "hello/index.html", params)

# # リスト3-18 p.198
# from django.shortcuts import render
# from .models import Friend
# from .forms import HelloForm

# def index(request):
#     data = Friend.objects.all().values("id", "name")
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# # リスト3-26 p.208
# from django.shortcuts import render
# from django.shortcuts import redirect
# from .models import Friend
# from .forms import HelloForm

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     params = {
#         "title":"Hello",
#         "form":HelloForm(),
#     }
#     if (request.method == "POST"):
#         name = request.POST["name"]
#         mail = request.POST["mail"]
#         gender = "gender" in request.POST
#         age = int(request.POST["age"])
#         birth = request.POST["birthday"]
#         friend = Friend(name = name, mail = mail, gender = gender,\
#                         age = age, birthday = birth)
#         friend.save()
#         return redirect(to = "/hello")
#     return render(request, "hello/create.html", params)

# # リスト3-29 p.213
# from django.shortcuts import render
# from django.shortcuts import redirect
# from .models import Friend
# from .forms import FriendForm

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# # リスト3-34 p.218
# from django.shortcuts import render
# from django.shortcuts import redirect
# from .models import Friend
# from .forms import FriendForm

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# # リスト3-38 p.223
# from django.shortcuts import render
# from django.shortcuts import redirect
# from .models import Friend
# from .forms import FriendForm

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# # リスト3-46 p.235
# from django.shortcuts import render
# from django.shortcuts import redirect

# from .models import Friend
# from .forms import FriendForm, FindForm

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         data = Friend.objects.filter(name = find)
#         msg = f"Result: {str(data.count())}"
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# # リスト3-47 p.238
# from django.shortcuts import render
# from django.shortcuts import redirect

# from .models import Friend
# from .forms import FriendForm, FindForm

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         data = Friend.objects.filter(name__icontains = find)
#         msg = f"Result: {str(data.count())}"
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# # リスト4-1 p.253
# from django.shortcuts import render
# from django.shortcuts import redirect

# from .models import Friend
# from .forms import FriendForm, FindForm

# def index(request):
#     data = Friend.objects.all().order_by("age")
#     params = {
#         "title":"Hello",
#         "message":"",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         data = Friend.objects.filter(name__icontains = find)
#         msg = f"Result: {str(data.count())}"
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# # リスト4-4 p.256
# from django.shortcuts import render
# from django.shortcuts import redirect

# from .models import Friend
# from .forms import FriendForm, FindForm

# def index(request):
#     data = Friend.objects.all().order_by("age")
#     params = {
#         "title":"Hello",
#         "message":"",
#         "data":data,
#     }
#     return render(request, "hello/index.html", params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         msg = "seach result:"
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         list = find.split()
#         data = Friend.objects.all()[int(list[0]):int(list[1])]
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# # リスト4-6 p.259
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Count,Sum,Avg,Min,Max

# from .models import Friend
# from .forms import FriendForm, FindForm

# def index(request):
#     data = Friend.objects.all()
#     re1 = Friend.objects.aggregate(Count('age'))
#     re2 = Friend.objects.aggregate(Sum('age'))
#     re3 = Friend.objects.aggregate(Avg('age'))
#     re4 = Friend.objects.aggregate(Min('age'))
#     re5 = Friend.objects.aggregate(Max('age'))

#     msg = f"count:{str(re1["age__count"])} \
#             <br>Sum:{str(re2["age__sum"])} \
#             <br>Average:{str(re3["age__avg"])} \
#             <br>Min:{str(re4["age__min"])} \
#             <br>Max:{str(re5["age__max"])}"
#     # msg = 'count:' + str(re1['age__count']) \
#     #     + '<br>Sum:' + str(re2['age__sum']) \
#     #     + '<br>Average:' + str(re3['age__avg']) \
#     #     + '<br>Min:' + str(re4['age__min']) \
#     #     + '<br>Max:' + str(re5['age__max'])
#     params = {
#     'title': 'Hello',
#     'message':msg,
#     'data': data,
#     }
#     return render(request, 'hello/index.html', params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         msg = "seach result:"
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         list = find.split()
#         data = Friend.objects.all()[int(list[0]):int(list[1])]
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# # リスト4-12 p.276
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Count, Sum, Avg, Min, Max

# from .models import Friend
# from .forms import FriendForm, FindForm, CheckForm

# def index(request):
#     data = Friend.objects.all()
#     re1 = Friend.objects.aggregate(Count('age'))
#     re2 = Friend.objects.aggregate(Sum('age'))
#     re3 = Friend.objects.aggregate(Avg('age'))
#     re4 = Friend.objects.aggregate(Min('age'))
#     re5 = Friend.objects.aggregate(Max('age'))
#     msg = f"count:{str(re1["age__count"])} \
#             <br>Sum:{str(re2["age__sum"])} \
#             <br>Average:{str(re3["age__avg"])} \
#             <br>Min:{str(re4["age__min"])} \
#             <br>Max:{str(re5["age__max"])}"
#     params = {
#     'title': 'Hello',
#     'message':msg,
#     'data': data,
#     }
#     return render(request, 'hello/index.html', params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         msg = "seach result:"
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         list = find.split()
#         data = Friend.objects.all()[int(list[0]):int(list[1])]
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# def check(request):
#     params = {
#     "title":"Hello",
#     "message":"check validation",
#     "form":CheckForm(),
#     }
#     if (request.method == "POST"):
#         form = CheckForm(request.POST)
#         params["form"] = form
#         if (form.is_valid()):
#             params["message"] = "OK!"
#         else:
#             params["message"] = "no good."
#     return render(request, "hello/check.html", params)

# # リスト4-21 p.289
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Count, Sum, Avg, Min, Max

# from .models import Friend
# from .forms import FriendForm, FindForm, CheckForm

# def index(request):
#     data = Friend.objects.all()
#     re1 = Friend.objects.aggregate(Count('age'))
#     re2 = Friend.objects.aggregate(Sum('age'))
#     re3 = Friend.objects.aggregate(Avg('age'))
#     re4 = Friend.objects.aggregate(Min('age'))
#     re5 = Friend.objects.aggregate(Max('age'))
#     msg = f"count:{str(re1["age__count"])} \
#             <br>Sum:{str(re2["age__sum"])} \
#             <br>Average:{str(re3["age__avg"])} \
#             <br>Min:{str(re4["age__min"])} \
#             <br>Max:{str(re5["age__max"])}"
#     params = {
#     'title': 'Hello',
#     'message':msg,
#     'data': data,
#     }
#     return render(request, 'hello/index.html', params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         msg = "seach result:"
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         list = find.split()
#         data = Friend.objects.all()[int(list[0]):int(list[1])]
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# def check(request):
#     params = {
#     "title":"Hello",
#     "message":"check validation.",
#     "form":FriendForm(),
#     }
#     if (request.method == "POST"):
#         obj = Friend()
#         form = FriendForm(request.POST, instance = obj)
#         params["form"] = form
#         if (form.is_valid()):
#             params["message"] = "OK!"
#         else:
#             params["message"] = "no good."
#     return render(request, "hello/check.html", params)

# # リスト4-31 p.309
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Count, Sum, Avg, Min, Max
# from django.core.paginator import Paginator

# from .models import Friend
# from .forms import FriendForm, FindForm, CheckForm

# def index(request, num = 1):
#     data = Friend.objects.all()
#     page = Paginator(data, 3)
#     params = {
#     'title': 'Hello',
#     'message':'',
#     'data': page.get_page(num),
#     }
#     return render(request, 'hello/index.html', params)

# def create(request):
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST)
#         print(friend)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "form":FriendForm(),
#     }
#     return render(request, "hello/create.html", params)

# def edit(request, num):
#     obj = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend = FriendForm(request.POST, instance = obj)
#         friend.save()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "form":FriendForm(instance = obj),
#     }
#     return render(request, "hello/edit.html", params)

# def delete(request, num):
#     friend = Friend.objects.get(id = num)
#     if (request.method == "POST"):
#         friend.delete()
#         return redirect(to = "/hello")
#     params = {
#     "title":"Hello",
#     "id":num,
#     "obj":friend,
#     }
#     return render(request, "hello/delete.html", params)

# def find(request):
#     if (request.method == "POST"):
#         msg = "seach result:"
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         list = find.split()
#         data = Friend.objects.all()[int(list[0]):int(list[1])]
#     else:
#         msg = "seach words..."
#         form = FindForm()
#         data = Friend.objects.all()
#     params ={
#         "title":"Hello",
#         "message": msg,
#         "form": form,
#         "data": data,
#     }
#     return render(request, "hello/find.html", params)

# def check(request):
#     params = {
#     "title":"Hello",
#     "message":"check validation.",
#     "form":FriendForm(),
#     }
#     if (request.method == "POST"):
#         obj = Friend()
#         form = FriendForm(request.POST, instance = obj)
#         params["form"] = form
#         if (form.is_valid()):
#             params["message"] = "OK!"
#         else:
#             params["message"] = "no good."
#     return render(request, "hello/check.html", params)

# リスト4-38 p.334
from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Avg, Min, Max
from django.core.paginator import Paginator

from .models import Friend, Message
from .forms import FriendForm, FindForm, CheckForm, MessageForm

def index(request, num = 1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message':'',
        'data': page.get_page(num),
    }
    return render(request, 'hello/index.html', params)

def create(request):
    if (request.method == "POST"):
        friend = FriendForm(request.POST)
        print(friend)
        friend.save()
        return redirect(to = "/hello")
    params = {
    "title":"Hello",
    "form":FriendForm(),
    }
    return render(request, "hello/create.html", params)

def edit(request, num):
    obj = Friend.objects.get(id = num)
    if (request.method == "POST"):
        friend = FriendForm(request.POST, instance = obj)
        friend.save()
        return redirect(to = "/hello")
    params = {
        "title":"Hello",
        "id":num,
        "form":FriendForm(instance = obj),
    }
    return render(request, "hello/edit.html", params)

def delete(request, num):
    friend = Friend.objects.get(id = num)
    if (request.method == "POST"):
        friend.delete()
        return redirect(to = "/hello")
    params = {
        "title":"Hello",
        "id":num,
        "obj":friend,
    }
    return render(request, "hello/delete.html", params)

def find(request):
    if (request.method == "POST"):
        msg = "seach result:"
        form = FindForm(request.POST)
        find = request.POST["find"]
        list = find.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        msg = "seach words..."
        form = FindForm()
        data = Friend.objects.all()
    params ={
        "title":"Hello",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "hello/find.html", params)

def check(request):
    params = {
    "title":"Hello",
    "message":"check validation.",
    "form":FriendForm(),
    }
    if (request.method == "POST"):
        obj = Friend()
        form = FriendForm(request.POST, instance = obj)
        params["form"] = form
        if (form.is_valid()):
            params["message"] = "OK!"
        else:
            params["message"] = "no good."
    return render(request, "hello/check.html", params)

def message(request, page = 1):
    if (request.method == "POST"):
        form = MessageForm(request.POST)
        form.save()
    data = Message.objects.all()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)