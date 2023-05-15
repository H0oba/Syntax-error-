# Generated by Django 4.2.1 on 2023-05-15 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_remove_attendance_attended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.subject'),
        ),
    ]