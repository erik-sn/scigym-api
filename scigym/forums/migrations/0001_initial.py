# Generated by Django 2.1.7 on 2019-09-11 15:09

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environments', '0015_auto_20190512_1003'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=30000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=30000)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('environment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='environments.Environment')),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.MessageBoard'),
        ),
    ]
