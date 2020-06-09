# Generated by Django 2.1.2 on 2020-05-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200524_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('4', '4'), ('2', '2'), ('3', '3'), ('1', '1')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('IS', 'IS'), ('RET', 'RET'), ('CSSE', 'CSSE')], max_length=12),
        ),
    ]
