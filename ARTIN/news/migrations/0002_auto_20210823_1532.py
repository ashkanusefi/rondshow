# Generated by Django 3.2 on 2021-08-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=70, verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(to='news.Category', verbose_name='نام دسته بندی'),
        ),
    ]
