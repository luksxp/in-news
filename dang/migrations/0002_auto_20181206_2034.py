# Generated by Django 2.1.1 on 2018-12-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(default=0),
        ),
        migrations.AddField(
            model_name='link',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
