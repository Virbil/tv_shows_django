# Generated by Django 2.2 on 2021-05-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0005_auto_20210524_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]