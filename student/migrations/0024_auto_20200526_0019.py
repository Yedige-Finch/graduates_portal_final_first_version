# Generated by Django 2.1.2 on 2020-05-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20200525_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(blank=True, choices=[('Part-time employment', 'Part-time employment'), ('Project work', 'Project work'), ('Internship', 'Internship'), ('Volunteering', 'Volunteering'), ('Full employment', 'Full employment')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(blank=True, choices=[('Remote work', 'Remote work'), ('Shift method', 'Shift method'), ('Shift work', 'Shift work'), ('Flexible schedule', 'Flexible schedule'), ('Full day', 'Full day')], max_length=100),
        ),
    ]
