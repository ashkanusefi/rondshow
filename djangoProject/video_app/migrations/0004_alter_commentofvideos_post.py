# Generated by Django 3.2.5 on 2021-07-28 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0003_commentofvideos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentofvideos',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_Videos', to='video_app.videos', verbose_name='نام ویدئو'),
        ),
    ]