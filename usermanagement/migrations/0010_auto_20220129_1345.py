# Generated by Django 3.1.6 on 2022-01-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0009_auto_20220129_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='ExamsCost',
            new_name='ExamCost',
        ),
        migrations.AlterField(
            model_name='patient',
            name='Service',
            field=models.CharField(choices=[('Generalist', 'Generalist'), ('Specialist', 'Specialist')], max_length=50, null=True),
        ),
    ]