# Generated by Django 3.1.6 on 2022-01-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0012_auto_20220129_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ConsultationCost',
            field=models.CharField(blank=True, default=2000, max_length=23, null=True),
        ),
    ]
