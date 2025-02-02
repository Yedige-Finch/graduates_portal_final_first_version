# Generated by Django 2.1.2 on 2020-05-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200520_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(choices=[('Volunteering', 'Volunteering'), ('Internship', 'Internship'), ('Project work', 'Project work'), ('Full employment', 'Full employment'), ('Part-time employment', 'Part-time employment')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(choices=[('Remote work', 'Remote work'), ('Shift work', 'Shift work'), ('Full day', 'Full day'), ('Shift method', 'Shift method'), ('Flexible schedule', 'Flexible schedule')], max_length=100),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=12),
        ),
    ]
