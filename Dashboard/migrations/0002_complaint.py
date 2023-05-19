# Generated by Django 4.2.1 on 2023-05-18 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='Dashboard.student')),
            ],
        ),
    ]
