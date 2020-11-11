# Generated by Django 3.0.5 on 2020-11-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_auto_20201109_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_likes', to='post.LikePost'),
        ),
    ]