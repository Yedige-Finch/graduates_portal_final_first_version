# Generated by Django 2.1.2 on 2020-05-20 16:55

import address.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_aboutstudent_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, null=True)),
                ('middle_name', models.CharField(max_length=127, null=True)),
                ('surname', models.CharField(max_length=127, null=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=12)),
                ('city', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
