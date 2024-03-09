from django.db import models

class Money(models.Model):
    use_date = models.DateTimeField('日付')
    detail = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    category = models.CharField(max_length=10)    # <- 追加

    def __str__(self):
        return self.detail + ' ￥' + str(self.cost)