# Generated by Django 4.1.5 on 2023-01-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
