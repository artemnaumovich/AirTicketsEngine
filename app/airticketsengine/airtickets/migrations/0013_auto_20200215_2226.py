# Generated by Django 3.0.2 on 2020-02-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtickets', '0012_auto_20200215_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
