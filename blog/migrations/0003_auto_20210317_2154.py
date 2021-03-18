# Generated by Django 3.1.7 on 2021-03-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='flagged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
