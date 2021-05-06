# Generated by Django 3.1.7 on 2021-05-06 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_auto_20210506_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleapp',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='custom_user.customuser'),
            preserve_default=False,
        ),
    ]
