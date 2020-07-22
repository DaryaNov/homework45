from django.db import models


class Article(models.Model):

    description = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    status = models.TextField(max_length=30, null=True, blank=False, default='new',verbose_name='Статус')
    date_completion = models.DateField(max_length=10, null=True,blank=False, verbose_name='Дата выполнения')


    def __str__(self):
        return "{}. {}".format(self.pk, self.status)


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
