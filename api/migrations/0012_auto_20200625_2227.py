# Generated by Django 3.0.7 on 2020-06-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_server_last_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='last_update_date',
            field=models.DateField(blank=True, null=True, verbose_name='最近汇报时间'),
        ),
    ]
