# Generated by Django 2.1.2 on 2020-05-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20200531_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='сс_approve',
            field=models.CharField(choices=[('N', 'N'), ('Y', 'Y')], default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('3', '3'), ('1', '1'), ('4', '4'), ('2', '2')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(choices=[('IS', 'IS'), ('CSSE', 'CSSE'), ('RET', 'RET')], max_length=12),
        ),
        migrations.AlterField(
            model_name='student',
            name='сс_approve',
            field=models.CharField(choices=[('N', 'N'), ('Y', 'Y')], default='N', max_length=1, null=True),
        ),
    ]
