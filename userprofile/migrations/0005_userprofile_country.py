# Generated by Django 4.0.1 on 2022-01-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_short_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]