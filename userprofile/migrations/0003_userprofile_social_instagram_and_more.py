# Generated by Django 4.0.1 on 2022-01-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='social_instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]