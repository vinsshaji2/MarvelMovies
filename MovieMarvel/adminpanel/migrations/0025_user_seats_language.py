# Generated by Django 4.1.5 on 2023-12-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0024_user_seats_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_seats',
            name='language',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
