from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    '''
    Новости
    '''
    list_display = ('text', 'time', 'theme')
    search_fields = ('text', 'theme')
    list_filter = ('time',)


admin.site.register(News, NewsAdmin)
