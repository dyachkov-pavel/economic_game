from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('news', views.NewsView)
router.register('teams', views.TeamsView)
router.register('maps', views.MapsView)
router.register('shares', views.ShareView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/stocks/<int:company_id>/', views.StockByTime.as_view()),
    path('v1/login/', views.TeamUserLoginView.as_view()),
]
