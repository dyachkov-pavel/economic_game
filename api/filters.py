from django_filters import rest_framework as filters
from news.models import News
from maps.models import Maps


class NewsFilter(filters.FilterSet):
    '''
    Фильтр новостей
    '''

    time = filters.TimeFilter(lookup_expr='lte')

    class Meta:
        model = News
        fields = ('time',)


class MapsFilter(filters.FilterSet):
    """
    Фильтр Карт
    """
    floor = filters.NumberFilter()
    corpus = filters.NumberFilter()

    class Meta:
        model = Maps
        fields = ('floor', 'corpus')
