# Generated by Django 3.0.5 on 2020-11-06 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0018_profile_working_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(related_name='user_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]