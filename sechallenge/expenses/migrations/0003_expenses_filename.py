# Generated by Django 2.0.2 on 2018-02-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20180225_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='filename',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
