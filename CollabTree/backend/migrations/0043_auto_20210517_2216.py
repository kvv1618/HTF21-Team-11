# Generated by Django 3.2.3 on 2021-05-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0042_auto_20210514_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='idea',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userattribs',
            name='full_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
