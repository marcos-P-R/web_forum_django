# Generated by Django 3.2 on 2021-04-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name_author',
            field=models.CharField(max_length=100),
        ),
    ]
