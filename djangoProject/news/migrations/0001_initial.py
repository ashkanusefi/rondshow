# Generated by Django 3.2.5 on 2021-07-26 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان خبر')),
                ('description', models.TextField(verbose_name='توضیحات خبر')),
                ('image', models.ImageField(upload_to='image_uploaded/', verbose_name='تصویر خبر')),
            ],
            options={
                'verbose_name': 'اخبار',
                'verbose_name_plural': 'اخبار',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('body', models.TextField(verbose_name='متن')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دیدگاه')),
                ('active', models.BooleanField(default=False, verbose_name='انتشار')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.new', verbose_name='عنوان خبر')),
            ],
            options={
                'verbose_name': 'نظرات',
                'verbose_name_plural': 'نظرات',
                'ordering': ['created_on'],
            },
        ),
    ]
