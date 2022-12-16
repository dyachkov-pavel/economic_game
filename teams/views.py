import datetime

from django.contrib.auth import authenticate, get_user_model, login
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.urls import reverse
from news.models import News

from .models import Operation, Share
from .forms import LoginForm


def index(request):
    if request.user.is_authenticated:
        operations = request.user.teams_operations.all().order_by('-id')
        shares = request.user.share_amount.all()
        return render(
            request,
            'index.html',
            context={
                'operations': operations,
                'shares': shares,
                'balance': request.user.teams_operations.all().aggregate(Sum('money'))}
        )
    return render(
        request,
        'index.html',
        {'error': False}
    )


def map(request):
    return render(
        request,
        'map_work.html',
    )


def news(request):
    time = datetime.datetime.now()
    time.replace(hour=(time.hour+3) % 24)
    news = News.objects.filter(
        time__lte=time
    ).order_by('-time')
    return render(
        request,
        'news.html',
        {'news': news}
    )


def rules(request):
    return render(
        request,
        'rules.html',
    )


def thanks(request):
    return render(
        request,
        'thanks.html',
    )


def shares(request):
    shares = Share.objects.all()
    return render(
        request,
        'shares.html',
        {'shares': shares}
    )


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
        return render(request, 'index.html', {'error': True})
    return render(request, 'index.html', {'error': False})
