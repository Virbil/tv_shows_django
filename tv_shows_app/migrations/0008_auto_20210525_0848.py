# Generated by Django 2.2 on 2021-05-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0007_auto_20210524_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
