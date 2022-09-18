from django.db import models

class Tasks(models.Model):
    description = models.CharField(verbose_name="Описание", max_length=200, null=False, blank=False)
    status = models.CharField(verbose_name="Статус", max_length=100, null=False, blank=False,default="No name")
    data_do = models.DateTimeField(verbose_name="Дата выполненияя", auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.status}"