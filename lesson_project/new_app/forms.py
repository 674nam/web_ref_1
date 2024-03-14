# # 演習問題
# from django import forms

# from .models import Member

# class MemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ["username", "phone", "age", "mail", ]

# class SeachForm(forms.Form):
#     seach = forms.CharField(label = "Seach", required = False, \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))

# class SortForm(forms.Form):
#     sort = [
#     ('id', 'IDの昇順'),
#     ('-id', 'IDの降順'),
#     ('age', 'Ageの昇順'),
#     ('-age', 'Ageの降順')
#     ]
#     choice = forms.ChoiceField(label = '並び替え', choices = sort)

# 演習 ※投稿機能を作成する
from django import forms

from .models import Member, Post, Category

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["username", "phone", "age", "mail", ]

class SeachForm(forms.Form):
    seach = forms.CharField(label = "Seach", required = False, \
        widget = forms.TextInput(attrs = {"class":"form-control"}))

class SortForm(forms.Form):
    sort = [
    ('id', 'IDの昇順'),
    ('-id', 'IDの降順'),
    ('age', 'Ageの昇順'),
    ('-age', 'Ageの降順')
    ]
    choice = forms.ChoiceField(label = '並び替え', choices = sort)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["category", "title","content", "member",]
        widgets = {
            "category":forms.Select(attrs = {"class":"form-control form-control-sm"}),
            "title":forms.TextInput(attrs = {"class":"form-control form-control-sm"}),
            "content":forms.Textarea(attrs = {"class":"form-control form-control-sm", "rows":2}),
            "member":forms.Select(attrs = {"class":"form-control form-control-sm"}),
        }

# おまけ※カテゴリーごとの絞込み機能、index関数(Post関数？)で絞込処理
class FilterForm(forms.Form):
    cate = Category.objects.all().values_list("name")
    choice = forms.ChoiceField(label = 'category', choices = cate)

