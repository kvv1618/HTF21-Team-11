# Generated by Django 3.1.7 on 2021-04-08 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_userattribs_assigned_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assigned_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user', to='backend.userattribs'),
        ),
    ]
