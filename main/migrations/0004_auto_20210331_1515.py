# Generated by Django 3.1.7 on 2021-03-31 15:15

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_post_zip_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=main.models.upload_file_name),
        ),
    ]
