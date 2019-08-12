# Generated by Django 2.2.3 on 2019-08-12 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190808_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='QQ',
            field=models.CharField(max_length=10, verbose_name='QQ号码'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(max_length=30, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]
