# Generated by Django 3.2.5 on 2021-07-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0004_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
