# Generated by Django 4.0 on 2022-01-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
