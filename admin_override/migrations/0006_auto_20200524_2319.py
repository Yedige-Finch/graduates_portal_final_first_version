# Generated by Django 2.1.2 on 2020-05-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_override', '0005_auto_20200524_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_question',
            field=models.CharField(max_length=512),
        ),
    ]
