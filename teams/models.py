from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager, PermissionsMixin)
from django.core.validators import MinValueValidator
from django.db import models


class Share(models.Model):
    '''
    Акция
    '''
    name = models.CharField('Название', max_length=100, unique=True)
    price = models.FloatField('Цена акции',
                              validators=[MinValueValidator(0), ])

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return f'{self.name} - {self.price}'


class TeamManager(BaseUserManager):

    def create_user(self, account, password, **other_fields):
        if not account:
            raise ValueError('Необходимо ввести номер счета')
        user = self.model(account=account, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, account, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        return self.create_user(account, password, **other_fields)


class TeamUser(AbstractBaseUser, PermissionsMixin):
    '''
    Личный кабинет команды
    '''
    name = models.CharField('Название команды', max_length=100, unique=True)
    account = models.IntegerField('Номер счёта', unique=True)
    balance = models.FloatField('Баланс', default=0)
    credit = models.BooleanField('Кредит', default=False)
    debit = models.BooleanField('Дебет', default=False)
    shares = models.ManyToManyField(Share,
                                    through='TeamShare',
                                    related_name='share_teams',
                                    verbose_name='Акции')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = []

    objects = TeamManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.name}, Номер счёта - {self.account}'


class Operation(models.Model):
    '''
    Операция
    '''
    money = models.FloatField('Сумма операции',)
    team = models.ForeignKey(TeamUser,
                             related_name='teams_operations',
                             on_delete=models.CASCADE,
                             verbose_name='Команды',)

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'{self.id} - {self.money}'


class TeamShare(models.Model):
    '''
    M2M Акции команд
    '''
    team = models.ForeignKey(TeamUser,
                             on_delete=models.CASCADE,
                             related_name='share_amount',
                             verbose_name='Команда')
    share = models.ForeignKey(Share,
                              on_delete=models.CASCADE,
                              related_name='teams_amount',
                              verbose_name='Акция')
    amount = models.IntegerField('Количество',
                                 validators=[MinValueValidator(0), ])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team', 'share'],
                name='one_share_per_team'
            )
        ]
        verbose_name = 'Акции команды'
        verbose_name_plural = 'Акции команды'

    def __str__(self) -> str:
        return f'{self.team} - {self.share}:{self.amount}'


class Quotes(models.Model):
    '''
    Котировки
    '''
    name = models.CharField('Название', max_length=100, blank=True)
    image = models.ImageField('Картинка', upload_to='images/')
    time = models.TimeField('Время')

    class Meta:
        verbose_name = 'Котировка'
        verbose_name_plural = 'Котировки'

    def __str__(self):
        return self.name
