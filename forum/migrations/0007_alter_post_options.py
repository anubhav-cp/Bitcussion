# Generated by Django 4.0.1 on 2022-01-20 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_post_isactive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
