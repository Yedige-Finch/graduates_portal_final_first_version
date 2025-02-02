# Generated by Django 2.1.2 on 2020-05-31 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0032_auto_20200531_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desiredposition',
            name='employment',
            field=models.CharField(blank=True, choices=[('Project work', 'Project work'), ('Full employment', 'Full employment'), ('Part-time employment', 'Part-time employment'), ('Volunteering', 'Volunteering'), ('Internship', 'Internship')], max_length=100),
        ),
        migrations.AlterField(
            model_name='desiredposition',
            name='schedule',
            field=models.CharField(blank=True, choices=[('Remote work', 'Remote work'), ('Shift method', 'Shift method'), ('Full day', 'Full day'), ('Flexible schedule', 'Flexible schedule'), ('Shift work', 'Shift work')], max_length=100),
        ),
        migrations.AlterField(
            model_name='photostudent',
            name='photo',
            field=models.ImageField(null=True, upload_to='student/media/uploads/'),
        ),
    ]
