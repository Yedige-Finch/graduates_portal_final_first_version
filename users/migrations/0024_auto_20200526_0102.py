# Generated by Django 2.1.2 on 2020-05-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20200526_0019'),
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
            field=models.CharField(choices=[('CSSE', 'CSSE'), ('IS', 'IS'), ('RET', 'RET')], max_length=12),
        ),
    ]
