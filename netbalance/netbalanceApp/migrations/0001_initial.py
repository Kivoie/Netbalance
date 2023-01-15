# Generated by Django 4.1.4 on 2023-01-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=128)),
                ('ip', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=8)),
                ('pending_add', models.BooleanField()),
                ('pending_delete', models.BooleanField()),
                ('description', models.CharField(max_length=128)),
            ],
        ),
    ]
