# Generated by Django 2.0.7 on 2019-05-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
