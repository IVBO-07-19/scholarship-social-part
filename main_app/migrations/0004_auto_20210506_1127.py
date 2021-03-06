# Generated by Django 3.1.7 on 2021-05-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_articleapp_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationsupportreport',
            name='central_service_id',
            field=models.IntegerField(default=1, verbose_name='Id центрального сервиса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onetimeparticipationreport',
            name='central_service_id',
            field=models.IntegerField(default=1, verbose_name='Id центрального сервиса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systematicreport',
            name='central_service_id',
            field=models.IntegerField(default=1, verbose_name='Id центрального сервиса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteerreport',
            name='central_service_id',
            field=models.IntegerField(default=1, verbose_name='Id центрального сервиса'),
            preserve_default=False,
        ),
    ]
