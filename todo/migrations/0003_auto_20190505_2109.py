# Generated by Django 2.0.7 on 2019-05-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='activity',
            field=models.TextField(),
        ),
    ]
