# Generated by Django 3.0.5 on 2020-10-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to='post.LikePost'),
        ),
    ]
