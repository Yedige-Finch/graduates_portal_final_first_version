# Generated by Django 2.1.2 on 2020-05-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20200525_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('2', '2'), ('1', '1')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('CSSE', 'CSSE'), ('IS', 'IS'), ('RET', 'RET')], max_length=12),
        ),
    ]
