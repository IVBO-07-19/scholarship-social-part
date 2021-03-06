# Generated by Django 3.1.7 on 2021-05-06 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_articlereport_central_service_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetimeparticipationapp',
            name='scores',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Баллы'),
        ),
        migrations.AddField(
            model_name='systematicapp',
            name='scores',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Баллы'),
        ),
        migrations.AddField(
            model_name='volunteerapp',
            name='scores',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Баллы'),
        ),
        migrations.CreateModel(
            name='Approvation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата оценивания')),
                ('opinion_score', models.SmallIntegerField(verbose_name='Субъективная оценка')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='informationsupportapp',
            name='approvation',
            field=models.ManyToManyField(blank=True, to='main_app.Approvation', verbose_name='Проверено'),
        ),
        migrations.AddField(
            model_name='onetimeparticipationapp',
            name='approvation',
            field=models.ManyToManyField(blank=True, to='main_app.Approvation', verbose_name='Проверено'),
        ),
        migrations.AddField(
            model_name='systematicapp',
            name='approvation',
            field=models.ManyToManyField(blank=True, to='main_app.Approvation', verbose_name='Проверено'),
        ),
        migrations.AddField(
            model_name='volunteerapp',
            name='approvation',
            field=models.ManyToManyField(blank=True, to='main_app.Approvation', verbose_name='Проверено'),
        ),
    ]
