# Generated by Django 3.1.7 on 2021-04-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210406_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
