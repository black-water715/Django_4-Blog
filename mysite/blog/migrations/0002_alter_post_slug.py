# Generated by Django 4.1.9 on 2023-05-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Введите slug-идентификатор', max_length=250, unique_for_date='publish', verbose_name='Идентификатор'),
        ),
    ]
