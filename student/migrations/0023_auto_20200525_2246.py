# Generated by Django 2.1.2 on 2020-05-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20200525_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(blank=True, choices=[('Full employment', 'Full employment'), ('Project work', 'Project work'), ('Internship', 'Internship'), ('Volunteering', 'Volunteering'), ('Part-time employment', 'Part-time employment')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(blank=True, choices=[('Flexible schedule', 'Flexible schedule'), ('Remote work', 'Remote work'), ('Full day', 'Full day'), ('Shift work', 'Shift work'), ('Shift method', 'Shift method')], max_length=100),
        ),
    ]
