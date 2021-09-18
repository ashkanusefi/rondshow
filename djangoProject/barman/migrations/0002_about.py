# Generated by Django 3.2.5 on 2021-07-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, verbose_name='عنوان')),
                ('section_one', models.TextField(verbose_name='توضیحات')),
                ('section_two', models.TextField(verbose_name='توضیحات')),
            ],
        ),
    ]