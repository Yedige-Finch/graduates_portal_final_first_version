# Generated by Django 2.1.2 on 2020-05-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200525_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('3', '3'), ('1', '1'), ('2', '2'), ('4', '4')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('RET', 'RET'), ('IS', 'IS'), ('CSSE', 'CSSE')], max_length=12),
        ),
    ]
