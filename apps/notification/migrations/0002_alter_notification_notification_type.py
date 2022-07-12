# Generated by Django 4.0.6 on 2022-07-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('message', 'Message'), ('follower', 'Follower'), ('like', 'Like'), ('mention', 'Mention')], max_length=20),
        ),
    ]
