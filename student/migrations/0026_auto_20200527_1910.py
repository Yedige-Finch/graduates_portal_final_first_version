# Generated by Django 2.1.2 on 2020-05-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_auto_20200526_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(blank=True, choices=[('Part-time employment', 'Part-time employment'), ('Full employment', 'Full employment'), ('Project work', 'Project work'), ('Volunteering', 'Volunteering'), ('Internship', 'Internship')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(blank=True, choices=[('Shift method', 'Shift method'), ('Flexible schedule', 'Flexible schedule'), ('Full day', 'Full day'), ('Remote work', 'Remote work'), ('Shift work', 'Shift work')], max_length=100),
        ),
    ]
