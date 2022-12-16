from django.db import models


class Maps(models.Model):
    """
    Карты
    """
    floor = models.IntegerField("Этаж")
    corpus = models.IntegerField("Корпус")
    urls_image = models.URLField("Ссылка на картинку")
    text_maps = models.TextField("Описание")

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return self.urls_image
