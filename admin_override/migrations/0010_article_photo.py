# Generated by Django 2.1.2 on 2020-06-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_override', '0009_auto_20200605_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(null=True, upload_to='admin_override/uploads/article'),
        ),
    ]
