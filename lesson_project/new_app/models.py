# # 演習問題
# from django.db import models

# class Member(models.Model):
#     username = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     age = models.IntegerField()
#     mail = models.EmailField(max_length=100)

#     def __str__(self):
#         return f'<Member:id={str(self.id)}, \
#             {self.username}({str(self.age)})>'

# 演習問題 ※バリデーション使用ver.
# from django.db import models
# from django.core.validators import MaxValueValidator

# class Member(models.Model):
#     username = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     age = models.IntegerField(validators=[MaxValueValidator(999)])
#     mail = models.EmailField(max_length=100)

#     def __str__(self):
#         return f'<Member:id={str(self.id)}, \
#             {self.username}({str(self.age)})>'

# 演習 ※投稿機能を作成する
from django.db import models
from django.core.validators import MaxValueValidator

class Member(models.Model):
    username = models.CharField(max_length=100)
    phone = models.IntegerField()
    age = models.IntegerField(validators=[MaxValueValidator(999)])
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return f'<Member:id={str(self.id)}, \
            {self.username}({str(self.age)})>'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 300)

    def __str__(self):
        return f"<Post:id={str(self.id)}, \
            {self.category},{self.title}({str(self.pub_date)})>"

    class Meta:
        ordering = ("pub_date",)