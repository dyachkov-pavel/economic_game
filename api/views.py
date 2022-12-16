from datetime import datetime, timezone

from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from maps.models import Maps
from news.models import News
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from stocks import img_map
from teams.models import Share

from . import filters as custom_filters
from . import serializers
from .responses import STOCKS_RESPONSE_SCHEMA, USER_RESPONSE_SCHEMA

TeamUser = get_user_model()


class ShareView(viewsets.ReadOnlyModelViewSet):
    '''
    Список акций
    '''
    queryset = Share.objects.all()
    serializer_class = serializers.ShareSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'name'

    def retrieve(self, request, name):
        share = get_object_or_404(self.get_queryset(), name__iexact=name)
        serializer = self.get_serializer(share)
        return Response(serializer.data)


class NewsView(viewsets.ReadOnlyModelViewSet):
    '''
    Список новостей
    '''
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = custom_filters.NewsFilter


class TeamsView(viewsets.ReadOnlyModelViewSet):
    '''
    Список команд
    '''
    queryset = TeamUser.objects.all().exclude(is_superuser=True)
    serializer_class = serializers.TeamSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'account'


class MapsView(viewsets.ReadOnlyModelViewSet):
    '''
    Карты
    '''
    queryset = Maps.objects.all()
    serializer_class = serializers.MapsSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = custom_filters.MapsFilter


class StockByTime(APIView):
    @swagger_auto_schema(responses=STOCKS_RESPONSE_SCHEMA)
    def get(self, request, company_id, format=None):
        hour = datetime.now(timezone.utc).hour + 3

        company_dict = img_map.get(company_id)
        if company_dict is None:
            return Response(data={'data': 'Wrong company id (number)'}, status=404)

        max_our = max(company_dict.keys())
        if hour - max_our < 2:
            hour = max_our

        link = company_dict.get(hour)
        if link is None:
            return Response(data={'data': 'No stocks now'}, status=204)

        return Response(data={'data': link}, status=200)


class TeamUserLoginView(APIView):
    @swagger_auto_schema(responses=USER_RESPONSE_SCHEMA,
                         request_body=serializers.TeamUserLoginSerializer)
    def post(self, request, format=None):
        serializer = serializers.TeamUserLoginSerializer(
            data=request.data,
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        account = request.data.get('account', None)
        password = request.data.get('password', None)
        teamuser = authenticate(account=account, password=password)
        return Response({'exists': True if teamuser else False})
