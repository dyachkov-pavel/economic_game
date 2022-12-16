from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Operation, Share, TeamShare, TeamUser, Quotes


class OperationAdmin(admin.ModelAdmin):
    '''
    Операция
    '''
    list_display = ('id', 'money', 'team',)
    list_filter = ('money', 'team',)


class OperationTabularAdmin(admin.TabularInline):
    '''
    Операция
    '''
    model = Operation
    extra = 1


class ShareAdmin(admin.ModelAdmin):
    '''
    Акция
    '''
    list_display = ('id', 'name', 'price',)
    search_fields = ('name',)
    list_filter = ('id', 'price',)


class ShareTabularAdmin(admin.TabularInline):
    '''
    Операция
    '''
    model = TeamUser.shares.through
    extra = 1


class TeamUserAdmin(UserAdmin):
    '''
    Команда
    '''
    list_display = ('id', 'name', 'account', 'balance',
                    'credit', 'debit', 'date_joined', )
    search_fields = ('id', 'name', 'account',)
    list_filter = ('id', 'account', 'credit', 'debit')
    ordering = ('date_joined',)
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('account', 'name', 'balance',
                           'credit', 'debit', 'date_joined', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser',),
        }),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('account', 'password1', 'password2'),
            },
        ),
    )
    inlines = (OperationTabularAdmin, ShareTabularAdmin, )


class TeamShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'share', 'amount',)
    search_fields = ('team', 'share',)
    list_filter = ('id', 'team', 'share', 'amount',)


admin.site.register(Operation, OperationAdmin)
admin.site.register(Share, ShareAdmin)
admin.site.register(TeamUser, TeamUserAdmin)
admin.site.register(TeamShare, TeamShareAdmin)
