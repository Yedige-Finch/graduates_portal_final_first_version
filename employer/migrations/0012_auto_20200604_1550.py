# Generated by Django 2.1.2 on 2020-06-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0011_auto_20200601_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='respond',
            name='employer_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='respond',
            name='respond_status_employer',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='respond',
            name='respond_status_student',
            field=models.CharField(default='Resume not viewed', max_length=512),
        ),
    ]
