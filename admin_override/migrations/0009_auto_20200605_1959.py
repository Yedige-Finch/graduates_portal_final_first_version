# Generated by Django 2.1.2 on 2020-06-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_override', '0008_auto_20200525_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='photo',
            field=models.ImageField(upload_to='admin_override/uploads/advice'),
        ),
    ]
