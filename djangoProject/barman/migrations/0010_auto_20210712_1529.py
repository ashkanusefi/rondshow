# Generated by Django 3.2.5 on 2021-07-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0009_auto_20210712_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cont',
            old_name='phone1',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='cont',
            name='phone2',
        ),
        migrations.RemoveField(
            model_name='cont',
            name='phone3',
        ),
        migrations.AddField(
            model_name='cont',
            name='instagram',
            field=models.CharField(blank=True, max_length=22, verbose_name='اینستاگرام'),
        ),
        migrations.AddField(
            model_name='cont',
            name='telegram',
            field=models.CharField(blank=True, max_length=22, verbose_name='تلگرام'),
        ),
    ]
