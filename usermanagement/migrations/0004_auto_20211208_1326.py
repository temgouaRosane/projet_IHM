# Generated by Django 3.1.6 on 2021-12-08 12:26

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0003_patient_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Status',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Student', 'Student'), ('other', 'other')], max_length=28, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='arterialPressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='numero',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
