# Generated by Django 2.1.2 on 2020-06-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20200604_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('3', '3'), ('2', '2'), ('4', '4'), ('1', '1')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('RET', 'RET'), ('IS', 'IS'), ('CSSE', 'CSSE')], max_length=12),
        ),
    ]
