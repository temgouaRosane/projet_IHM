# Generated by Django 3.2.9 on 2021-12-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Time',
            field=models.TimeField(auto_now=True),
        ),
    ]