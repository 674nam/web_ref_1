# from django.shortcuts import render, redirect
# from django.utils import timezone

# def index(request):
#     today = str(timezone.now()).split('-')
#     context = {
#         'year' : today[0],
#         'month' : today[1],
#     }
#     return render(request, 'money/index.html', context)


# from django.shortcuts import render, redirect
# from django.utils import timezone

# from .models import Money

# def index(request):
#     today = str(timezone.now()).split('-')
#     money = Money.objects.all()
#     for m in money:
#         date = str(m.use_date).split(' ')[0]
#         m.use_date = '/'.join(date.split('-')[1:3])
#     context = {'year' : today[0],
#             'month' : today[1],
#             'money' : money,
#     }
#     return render(request, 'money/index.html', context)

from django.shortcuts import render, redirect
from django.utils import timezone
# import pytz
import datetime

from .models import Money
from .forms import SpendingForm

def index(request):
    today = str(timezone.now()).split('-')
    money = Money.objects.all()
    for m in money:
        date = str(m.use_date).split(' ')[0]
        m.use_date = '/'.join(date.split('-')[1:3])

    form = SpendingForm()    #フォームを読み込む
    context = {'year' : today[0],
            'month' : today[1],
            'money' : money,
            'form' : form
            }

    if request.method == 'POST':    # フォームでデータが送られてきたら
        data = request.POST
        use_date = data['use_date']
        cost = data['cost']
        detail = data['detail']
        use_date = timezone.datetime.strptime(use_date, "%Y/%m/%d")
        # tokyo_timezone = pytz.timezone('Asia/Tokyo')    #タイムゾーンを設定
        # use_date = tokyo_timezone.localize(use_date)
        # use_date += datetime.timedelta(hours=9)    #時間を9時間遅らせる

        Money.objects.create(    # データベースにデータを入れる
                use_date = use_date,
                detail = detail,
                cost = int(cost),
                )
        return redirect(to='/money/')    #再び/money/を読み込む

    return render(request, 'money/index.html', context)