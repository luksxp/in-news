# Generated by Django 2.1.1 on 2018-12-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dang', '0005_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
