# Generated by Django 3.2.5 on 2021-07-13 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_sub_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service', verbose_name='نام سردسته'),
        ),
    ]
