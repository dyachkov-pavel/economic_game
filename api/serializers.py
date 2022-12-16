from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_serializer_method
from maps.models import Maps
from news.models import News
from rest_framework import serializers
from teams.models import Operation, Share, TeamShare, TeamUser

TeamUser = get_user_model()


class TeamUserLoginSerializer(serializers.Serializer):
    '''
    Сериализатор новостей
    '''
    account = serializers.IntegerField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class NewsSerializer(serializers.ModelSerializer):
    '''
    Сериализатор новостей
    '''

    class Meta:
        model = News
        fields = ('id', 'text', 'theme', 'time', )


class OperationSerializer(serializers.ModelSerializer):
    '''
    Сериализатор операций
    '''
    class Meta:
        model = Operation
        fields = ('id', 'money',)


class ShareSerializer(serializers.ModelSerializer):
    '''
    Сериализатор Акций
    '''
    class Meta:
        model = Share
        fields = ('name', 'price', )


class TeamShareSerializer(serializers.ModelSerializer):
    '''
    Сериализатор Акций Команд
    '''
    share = ShareSerializer()

    class Meta:
        model = TeamShare
        fields = ('share', 'amount', )


class TeamSerializer(serializers.ModelSerializer):
    '''
    Сериализатор команд
    '''
    operations = serializers.SerializerMethodField()
    shares = serializers.SerializerMethodField()

    class Meta:
        model = TeamUser
        fields = ('id', 'name', 'account', 'balance', 'credit',
                  'debit', 'operations', 'shares', )

    @swagger_serializer_method(serializer_or_field=TeamShareSerializer)
    def get_shares(self, obj):
        shares_query = TeamShare.objects.filter(team_id=obj.id)
        serializer = TeamShareSerializer(shares_query, many=True)
        return serializer.data

    @swagger_serializer_method(serializer_or_field=OperationSerializer)
    def get_operations(self, obj):
        operations_query = Operation.objects.filter(team_id=obj.id)
        serializer = OperationSerializer(operations_query, many=True)
        return serializer.data


class MapsSerializer(serializers.ModelSerializer):
    """
    Сериализатор карт
    """
    class Meta:
        model = Maps
        fields = ('floor', 'corpus', 'urls_image', 'text_maps')
