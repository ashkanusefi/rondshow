# Generated by Django 3.2.5 on 2021-07-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام نمونه کار')),
                ('description', models.TextField(verbose_name='توضیحات نمونه کار')),
                ('image', models.ImageField(upload_to='image_uploaded/', verbose_name='تصویر نمونه کار')),
            ],
            options={
                'verbose_name': 'نمونه کار',
                'verbose_name_plural': 'نمونه کار',
            },
        ),
    ]
