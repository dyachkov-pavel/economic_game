from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('map/', views.map, name='map'),
    path('news/', views.news, name='news'),
    path('rules/', views.rules, name='rules'),
    path('shares/', views.shares, name='shares'),
    path('thanks/', views.thanks, name='thanks'),
]
