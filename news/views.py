from django.shortcuts import render
from django.utils import timezone
from news.models import Post, IndicationsDate, Area, Indications, Subscriber
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import AddIndicationsForm, SubscribeForm


# Create your views here.


def news_list(request):
    subscribe_form = SubscribeForm(request.POST or None)
    if request.method == 'POST':
        if subscribe_form.is_valid():
            address = request.POST['email']
            subscriber = Subscriber.objects.filter(email=address)
            if not subscriber:
                subscriber = Subscriber(email=address)
                subscriber.save()
                return HttpResponseRedirect('/')
    posts = Post.objects.all()
    return render(request, 'news/news_list.html', {'posts': posts, 'subscribe_form': subscribe_form})


def home(request):
    return render(request, 'news/home.html', {})


def payinfo(request):
    number = 0
    if request.method == 'POST':
        number = request.POST['area_number']
    data = {}
    debts = {}
    if number:
        data['number'] = number
        debts = [
            {'title': 'Электроэнергия', 'value': 1275.64},
            {'title': 'Членские взносы', 'value': 5467.22},
            {'title': 'ТО газового хозяйства', 'value': 7000.00},
        ]
    return render(request, 'news/payinfo.html', {'data': data, 'debts': debts})


def directorate(request):
    items = Area.objects.filter(dir_fl=True).order_by('owner')
    return render(request, 'news/directorate.html', {'items': items})


def snt(request):
    items = [{'title': 'Контакты', 'ref': '\home'},
             {'title': 'Правление', 'ref': '\directorate'},
             {'title': 'Ревизионная комиссия', 'ref': '#'},
             {'title': 'Устав товарищества', 'ref': '#'},
             {'title': 'Протоколы общих собраний', 'ref': '#'},
             {'title': 'Протоколы собраний правления', 'ref': '#'}]
    return render(request, 'news/snt.html', {'items': items})


def new_indications(request):
    # Если данный запрос типа POST, тогда
    if request.method == 'POST':
        form = AddIndicationsForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            ind_date_obj = IndicationsDate(date=date)
            ind_date_obj.save()
            ind_data = form.cleaned_data['indications']
            ind_list = [s for s in ind_data.splitlines() if s]
            for sind in ind_list:
                ind = sind.split()
                if len(ind) == 3:
                    area = Area.objects.filter(number=ind[0])
                    if len(area) == 1:
                        ind_obj = Indications(date=ind_date_obj, area=area[0], T1=ind[1], T2=ind[2])
                        ind_obj.save()
            return HttpResponseRedirect('/')

    else:
        form = AddIndicationsForm()
    return render(request, 'news/new_indications.html', {'form': form})
