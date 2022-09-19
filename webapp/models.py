from django.db import models


class Tasks(models.Model):

    SET_STATUS = [
        ('Done', 'Выполнено'),
        ('During', 'В процессе'),
        ('New', 'Не начата'),
    ]

    description = models.CharField(verbose_name="Описание", max_length=200, null=False, blank=False)
    # status = models.CharField(verbose_name="Статус", max_length=100, choices=SET_STATUS , null=False, blank=False, default="NS")
    set_st = models.CharField(verbose_name='Статус', max_length=9, choices=SET_STATUS)
    data_do = models.DateField(verbose_name="Дата выполненияя", auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.set_st} - {self.data_do}"
