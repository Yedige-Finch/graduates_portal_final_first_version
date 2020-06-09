# Generated by Django 2.1.2 on 2020-05-31 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0009_auto_20200531_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respond',
            name='respond_status_employer',
            field=models.CharField(choices=[('2', 'Resume viewed'), ('1', 'Resume not viewed'), ('3', 'Renouncement')], max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='respond',
            name='respond_status_student',
            field=models.CharField(choices=[('2', 'Resume viewed'), ('1', 'Resume not viewed'), ('3', 'Renouncement')], default='Resume not viewed', max_length=512),
        ),
    ]
