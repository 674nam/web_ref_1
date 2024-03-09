import calendar
import datetime
from django.shortcuts import render, redirect
from django.utils import timezone

import matplotlib.pyplot as plt # pip install必要
import pytz # pip install必要

from .models import Money
from .forms import SpendingForm

plt.rcParams['font.family'] = 'MS Gothic' #日本語フォント表示

def index(request, year=None, month=None):
    if year is None or month is None:
        today = timezone.now()
        year = today.year
        month = today.month
    else:
        year = int(year)
        month = int(month)

    money = Money.objects.filter(use_date__year=year, use_date__month=month).order_by('use_date')
    total = 0
    for m in money:
        date = m.use_date.strftime('%m/%d')
        m.use_date = date
        total += m.cost

    form = SpendingForm()

    next_year, next_month = get_next(year, month)
    prev_year, prev_month = get_prev(year, month)

    context = {'year' : year,
            'month' : month,
            'prev_year' : prev_year,
            'prev_month' : prev_month,
            'next_year' : next_year,
            'next_month' : next_month,
            'money' : money,
            'total' : total,
            'form' : form
            }

    draw_graph(year, month)

    if request.method == 'POST':
        data = request.POST
        use_date = data['use_date']
        cost = data['cost']
        detail = data['detail']
        category = data['category']

        use_date = datetime.datetime.strptime(use_date, "%Y/%m/%d")
        tokyo_timezone = pytz.timezone('Asia/Tokyo')
        use_date = tokyo_timezone.localize(use_date)
        use_date += datetime.timedelta(hours=9)

        Money.objects.create(
            use_date=use_date,
            detail=detail,
            cost=int(cost),
            category=category,
        )
        return redirect(to='/money/{}/{}/'.format(year, month))

    return render(request, 'money/index.html', context)


def get_next(year, month):
    year = int(year)
    month = int(month)

    if month == 12:
        return str(year + 1), '1'
    else:
        return str(year), str(month + 1)


def get_prev(year, month):
    year = int(year)
    month = int(month)
    if month == 1:
        return str(year - 1), '12'
    else:
        return str(year), str(month - 1)


def draw_graph(year, month):
    money = Money.objects.filter(use_date__year=year, use_date__month=month).order_by('use_date')
    last_day = calendar.monthrange(year, month)[1] + 1
    day = list(range(1, last_day))
    cost = [0] * len(day)
    for m in money:
        day_index = m.use_date.day - 1
        cost[day_index] += m.cost

    plt.figure()
    plt.bar(day, cost, color='#00bfff', edgecolor='#0000ff')
    plt.grid(True)
    plt.xlim([0, last_day])
    plt.xlabel('日付', fontsize=16)
    plt.ylabel('支出額(円)', fontsize=16)

    # static/imagesフォルダに保存
    plt.savefig('money/static/images/bar_{}_{}.svg'.format(year, month), transparent=True)
