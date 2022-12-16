from django.db import models


class News(models.Model):
    '''
    Новости
    '''
    text = models.TextField('Текст')
    theme = models.CharField('Тематика', max_length=50)
    # image = models.ImageField('Картинка', upload_to='images/')
    time = models.TimeField('Время')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.text[:15]
