# Generated by Django 2.1.2 on 2020-05-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_override', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='photo',
            field=models.ImageField(default='some', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
