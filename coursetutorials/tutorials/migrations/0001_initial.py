# Generated by Django 3.2.8 on 2021-10-10 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_title', models.CharField(max_length=120)),
                ('series_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('video_url', models.CharField(max_length=150)),
                ('individual', models.BooleanField(default=True)),
                ('series', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tutorials.tutorialseries')),
            ],
        ),
    ]
