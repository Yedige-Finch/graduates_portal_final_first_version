# Generated by Django 2.1.2 on 2020-05-22 20:15

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20200523_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Full employment', 'Full employment'), ('Volunteering', 'Volunteering'), ('Project work', 'Project work'), ('Part-time employment', 'Part-time employment')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(choices=[('Flexible schedule', 'Flexible schedule'), ('Full day', 'Full day'), ('Shift work', 'Shift work'), ('Remote work', 'Remote work'), ('Shift method', 'Shift method')], max_length=100),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='city',
            field=address.models.AddressField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=12, null=True),
        ),
    ]
