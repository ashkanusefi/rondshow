# Generated by Django 3.2.5 on 2021-07-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0011_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]