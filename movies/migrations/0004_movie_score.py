# Generated by Django 2.2.4 on 2019-08-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190823_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
