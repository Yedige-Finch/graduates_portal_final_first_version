# Generated by Django 2.1.2 on 2020-05-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_override', '0003_auto_20200524_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='themes',
            new_name='topic',
        ),
        migrations.AddField(
            model_name='advice',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
