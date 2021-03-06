# Generated by Django 3.2.5 on 2021-07-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0007_auto_20210712_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contac_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیح تماس با ما')),
                ('phone1', models.CharField(blank=True, max_length=22, verbose_name='شماره تماس اول')),
                ('phone2', models.CharField(blank=True, max_length=22, verbose_name='شماره تماس دوم')),
                ('phone3', models.CharField(blank=True, max_length=22, verbose_name='شماره تماس سوم')),
                ('address', models.TextField(verbose_name='ادرس')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='ایمیل')),
            ],
        ),
    ]
