# Generated by Django 3.2.5 on 2021-07-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barman', '0008_contac_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, verbose_name='توضیح تماس با ما')),
                ('phone1', models.CharField(blank=True, max_length=22, verbose_name='شماره تماس اول')),
                ('phone2', models.CharField(blank=True, max_length=22, verbose_name='شماره تماس دوم')),
                ('phone3', models.CharField(blank=True, max_length=22, verbose_name='شماره تماس سوم')),
                ('address', models.TextField(verbose_name='ادرس')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='ایمیل')),
            ],
        ),
        migrations.DeleteModel(
            name='Contac_Us',
        ),
    ]
