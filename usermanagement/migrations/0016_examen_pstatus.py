# Generated by Django 3.1.6 on 2022-02-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0015_auto_20220131_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='pstatus',
            field=models.CharField(default='invalid', max_length=20),
        ),
    ]