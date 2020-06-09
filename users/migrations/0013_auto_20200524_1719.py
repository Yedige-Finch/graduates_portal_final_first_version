# Generated by Django 2.1.2 on 2020-05-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200524_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('RET', 'RET'), ('IS', 'IS'), ('CSSE', 'CSSE')], max_length=12),
        ),
    ]
