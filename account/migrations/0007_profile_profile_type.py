# Generated by Django 3.0.5 on 2020-09-06 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_profile_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.ProfileType'),
        ),
    ]
