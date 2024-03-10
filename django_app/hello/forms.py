# # リスト2-28 p.100
# from django import forms

# class HelloForm(forms.Form):
#     name = forms.CharField(label="name")
#     mail = forms.CharField(label="mail")
#     age = forms.IntegerField(label="age")

# # リスト2-33 p.108
# from django import forms

# class HelloForm(forms.Form):
#     name = forms.CharField(label="name", \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))
#     mail = forms.CharField(label="mail", \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))
#     age = forms.IntegerField(label="age", \
#         widget = forms.NumberInput(attrs = {"class":"form-control"}))

# # リスト3-12 p.189
# from django import forms

# class HelloForm(forms.Form):
#     id = forms.IntegerField(label="ID")

# # リスト3-23 p.205
# from django import forms

# class HelloForm(forms.Form):
#     name = forms.CharField(label="Name", \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))
#     mail = forms.EmailField(label="Email", \
#         widget = forms.EmailInput(attrs = {"class":"form-control"}))
#     gender = forms.BooleanField(label="Gender", required = False, \
#         widget = forms.CheckboxInput(attrs = {"class":"form-check"}))
#     age = forms.IntegerField(label="Age", \
#         widget = forms.NumberInput(attrs = {"class":"form-control"}))
#     birthday = forms.DateField(label="Birth", \
#         widget = forms.DateInput(attrs = {"class":"form-control"}))

# # リスト3-28 p.212
# from django import forms
# from .models import Friend

# class FriendForm(forms.ModelForm):
#     class Meta:
#         model = Friend
#         fields = ["name", "mail", "gender", "age", "birthday"]

# # リスト3-44 p.233
# from django import forms
# from .models import Friend

# class FriendForm(forms.ModelForm):
#     class Meta:
#         model = Friend
#         fields = ["name", "mail", "gender", "age", "birthday"]

# class FindForm(forms.Form):
#     find = forms.CharField(label="Find", required = False, \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))

# # リスト4-11 p.276
# from django import forms
# from .models import Friend

# class FriendForm(forms.ModelForm):
#     class Meta:
#         model = Friend
#         fields = ["name", "mail", "gender", "age", "birthday"]

# class FindForm(forms.Form):
#     find = forms.CharField(label="Find", required = False, \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))

# class CheckForm(forms.Form):
#     find = forms.CharField(label="Name", \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))

# # リスト4-28 p.303
# from django import forms
# from .models import Friend

# class FriendForm(forms.ModelForm):
#     class Meta:
#         model = Friend
#         fields = ["name", "mail", "gender", "age", "birthday"]
#         widgets = {
#             "name":forms.TextInput(attrs = {"class":"form-control"}),
#             "mail":forms.EmailInput(attrs = {"class":"form-control"}),
#             "age":forms.NumberInput(attrs = {"class":"form-control"}),
#             "birthday":forms.DateInput(attrs = {"class":"form-control"}),
#         }

# class FindForm(forms.Form):
#     find = forms.CharField(label="Find", required = False, \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))

# class CheckForm(forms.Form):
#     find = forms.CharField(label="Name", \
#         widget = forms.TextInput(attrs = {"class":"form-control"}))

# リスト4-37 p.333
from django import forms
from .models import Friend, Message

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "mail", "gender", "age", "birthday"]
        widgets = {
            "name":forms.TextInput(attrs = {"class":"form-control"}),
            "mail":forms.EmailInput(attrs = {"class":"form-control"}),
            "age":forms.NumberInput(attrs = {"class":"form-control"}),
            "birthday":forms.DateInput(attrs = {"class":"form-control"}),
        }

class FindForm(forms.Form):
    find = forms.CharField(label="Find", required = False, \
        widget = forms.TextInput(attrs = {"class":"form-control"}))

class CheckForm(forms.Form):
    find = forms.CharField(label="Name", \
        widget = forms.TextInput(attrs = {"class":"form-control"}))
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content", "friend",]
        widgets = {
            "title":forms.TextInput(attrs = {"class":"form-control form-control-sm"}),
            "content":forms.Textarea(attrs = {"class":"form-control form-control-sm", "rows":2}),
            "friend":forms.Select(attrs = {"class":"form-control form-control-sm"}),
        }