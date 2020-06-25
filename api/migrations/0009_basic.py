# Generated by Django 3.0.7 on 2020-06-25 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200625_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=32, verbose_name='系统类型')),
                ('version', models.CharField(max_length=128, verbose_name='发行版')),
                ('cpu_count', models.IntegerField(verbose_name='CPU个数')),
                ('kernel_version', models.CharField(max_length=128, verbose_name='内核版本')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server')),
            ],
        ),
    ]
