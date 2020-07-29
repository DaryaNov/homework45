from django.db import models


STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]



class Article(models.Model):

    description = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    maxdescription = models.TextField(max_length=2000,null=True,blank=False,verbose_name='Подробное описание')
    status = models.TextField(max_length=30,choices=STATUS_CHOICES, default='new',verbose_name='Статус')
    date_completion = models.CharField(max_length=10, null=False,blank=False,default='none', verbose_name='Дата выполнения')


    def __str__(self):
        return "{}. {}".format(self.pk, self.status)


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'