# Generated by Django 4.0 on 2022-01-12 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('forum', '0003_rename_tags_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile'),
        ),
    ]
