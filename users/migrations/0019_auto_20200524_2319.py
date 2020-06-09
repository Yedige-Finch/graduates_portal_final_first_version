# Generated by Django 2.1.2 on 2020-05-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200524_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('1', '1'), ('2', '2')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('RET', 'RET'), ('CSSE', 'CSSE'), ('IS', 'IS')], max_length=12),
        ),
    ]
