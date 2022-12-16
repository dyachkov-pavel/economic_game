from django.urls import path

from . import views


urlpatterns = [
    path('loaddata/', views.update_data, name='update_data'),
]
