# Generated by Django 3.1.7 on 2021-07-07 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0006_alter_skillsubcategory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barman.menu')),
            ],
        ),
        migrations.RemoveField(
            model_name='skillsubcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='SkillCategory',
        ),
        migrations.DeleteModel(
            name='SkillSubCategory',
        ),
    ]
