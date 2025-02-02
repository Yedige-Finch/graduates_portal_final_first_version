# Generated by Django 2.1.2 on 2020-05-29 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20200530_0018'),
        ('employer', '0004_respond'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCompany',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Company')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteVacancy',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
                ('vac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='UndesirableCompany',
            fields=[
                ('und_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Company')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
        migrations.CreateModel(
            name='UndesirableVacancy',
            fields=[
                ('und_id', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
                ('vac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Vacancy')),
            ],
        ),
        migrations.AlterField(
            model_name='respond',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
