# Generated by Django 3.0.7 on 2020-06-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
