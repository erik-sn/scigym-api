# Generated by Django 2.1.7 on 2019-09-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_auto_20190925_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='title_url',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
