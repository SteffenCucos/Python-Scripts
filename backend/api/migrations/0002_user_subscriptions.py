# Generated by Django 2.1 on 2018-08-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscriptions',
            field=models.CharField(blank=True, default=None, max_length=5000, null=True),
        ),
    ]