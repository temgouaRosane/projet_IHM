# Generated by Django 3.1.6 on 2022-01-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0010_auto_20220129_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='ExamCost',
        ),
        migrations.AlterField(
            model_name='patient',
            name='ConsultationCost',
            field=models.FloatField(blank=True, max_length=23, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Service',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
