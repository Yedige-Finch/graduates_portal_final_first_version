# Generated by Django 2.1.2 on 2020-05-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200523_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('IS', 'IS'), ('CSSE', 'CSSE'), ('RET', 'RET')], max_length=12),
        ),
    ]
