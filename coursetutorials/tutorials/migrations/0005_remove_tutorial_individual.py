# Generated by Django 3.2.8 on 2021-10-11 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_alter_tutorial_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='individual',
        ),
    ]
