
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('status', models.CharField(default='No name', max_length=100, verbose_name='Статус')),
                ('data_do', models.DateTimeField(auto_now_add=True, verbose_name='Дата выполненияя')),
            ],
        ),
    ]
