# Generated by Django 2.1.2 on 2020-05-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20200524_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(blank=True, choices=[('Full employment', 'Full employment'), ('Internship', 'Internship'), ('Project work', 'Project work'), ('Part-time employment', 'Part-time employment'), ('Volunteering', 'Volunteering')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(blank=True, choices=[('Remote work', 'Remote work'), ('Shift method', 'Shift method'), ('Full day', 'Full day'), ('Flexible schedule', 'Flexible schedule'), ('Shift work', 'Shift work')], max_length=100),
        ),
    ]
