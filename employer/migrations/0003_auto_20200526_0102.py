# Generated by Django 2.1.2 on 2020-05-25 19:02

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20200526_0102'),
        ('address', '0002_auto_20160213_1726'),
        ('employer', '0002_auto_20200526_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('vac_id', models.AutoField(primary_key=True, serialize=False)),
                ('vacancy_name', models.CharField(max_length=512, null=True)),
                ('salary', models.CharField(max_length=512, null=True)),
                ('company_name', models.CharField(max_length=512, null=True)),
                ('experience', models.TextField(null=True)),
                ('about', models.TextField(null=True)),
                ('duties', models.TextField(null=True)),
                ('Requirements', models.TextField(null=True)),
                ('work_condition', models.TextField(null=True)),
                ('skills', models.TextField(null=True)),
                ('contacts_phone', models.CharField(max_length=512, null=True)),
                ('contact_mail', models.CharField(max_length=512, null=True)),
                ('publication_date', models.DateField(auto_now_add=True, null=True)),
                ('upd_date', models.DateField(auto_now=True, null=True)),
                ('address', address.models.AddressField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Employer')),
            ],
        ),
        migrations.RenameField(
            model_name='company',
            old_name='about',
            new_name='about_company',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='comp_id',
            new_name='company_id',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='comp_mail',
            new_name='company_mail',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='comp_name',
            new_name='company_name',
        ),
        migrations.AlterField(
            model_name='company',
            name='contacts_phone',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
