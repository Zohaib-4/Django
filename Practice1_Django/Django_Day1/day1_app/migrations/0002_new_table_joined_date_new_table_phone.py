# Generated by Django 5.1 on 2024-08-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day1_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_table',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='new_table',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
