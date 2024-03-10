# # リスト5-4 p.362
# from django import forms
# from .models import Message, Good
# from django.contrib.auth.models import User

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ["content",]

# # index.htmlのフォームを直してください。
# # Chapter4のmessage関数、MessageFormあたりを参考にして下さい。
from django import forms
from .models import Message, Good
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content",]
        widgets ={
            "content":forms.Textarea(attrs={"class":"form-control form-control-sm",\
            "rows":1})
        }