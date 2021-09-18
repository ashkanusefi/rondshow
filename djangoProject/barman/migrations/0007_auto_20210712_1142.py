# Generated by Django 3.2.5 on 2021-07-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0006_auto_20210712_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='ab',
            name='name_two',
            field=models.CharField(blank=True, max_length=200, verbose_name='عنوان بخش دوم'),
        ),
        migrations.AddField(
            model_name='ab',
            name='section_one',
            field=models.TextField(blank=True, verbose_name='توضیحات بخش اول'),
        ),
        migrations.AddField(
            model_name='ab',
            name='section_two',
            field=models.TextField(blank=True, verbose_name='توضیحات بخش دوم'),
        ),
    ]