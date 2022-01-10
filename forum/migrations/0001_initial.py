# Generated by Django 4.0 on 2022-01-10 18:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('description', models.CharField(max_length=2000)),
                ('upvote', models.IntegerField(blank=True, default=0, null=True)),
                ('downvote', models.IntegerField(blank=True, default=0, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solutions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.solution')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=2000)),
                ('upvote', models.IntegerField(blank=True, default=0, null=True)),
                ('downvote', models.IntegerField(blank=True, default=0, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='forum.Tags')),
            ],
        ),
    ]
