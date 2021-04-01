# Generated by Django 3.1.7 on 2021-04-01 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название статьи')),
                ('media_title', models.CharField(max_length=255, verbose_name='Название источника СМИ')),
                ('edition_level_choicer', models.CharField(choices=[('university', 'университетский'), ('municipal', 'городской')], max_length=255, verbose_name='Уровень издания')),
                ('co_author_quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество соавторов')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='InformationSupportReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('work', models.TextField(verbose_name='Выполненные работы по мероприятию')),
                ('start_date', models.DateField(verbose_name='Начало выполнения деятельности')),
                ('final_date', models.DateField(verbose_name='Конец выполнения деятельности')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OneTimeParticipationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('work', models.TextField(verbose_name='Выполненные работы по мероприятию')),
                ('date', models.DateField(verbose_name='Даты проведения')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystematicReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('work', models.TextField(verbose_name='Выполненные работы по мероприятию')),
                ('start_date', models.DateField(verbose_name='Начало выполнения деятельности')),
                ('final_date', models.DateField(verbose_name='Конец выполнения деятельности')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VolunteerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('work', models.TextField(verbose_name='Выполненные работы по мероприятию')),
                ('date', models.DateField(verbose_name='Даты проведения')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VolunteerApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=255, verbose_name='ФИО и должность лица, подтверждающего участие')),
                ('is_leader', models.BooleanField(default=False, verbose_name='Руководитель')),
                ('is_organizer', models.BooleanField(default=False, verbose_name='Организатор')),
                ('is_teamleader', models.BooleanField(default=False, verbose_name='Тимлидер')),
                ('is_volunteer', models.BooleanField(default=False, verbose_name='Волонтёр')),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.volunteerreport', verbose_name='Отчёт')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystematicApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=255, verbose_name='ФИО и должность лица, подтверждающего участие')),
                ('is_organizer', models.BooleanField(default=False, verbose_name='Организатор')),
                ('is_co_organizer', models.BooleanField(default=False, verbose_name='Соорганизатор')),
                ('is_assistant', models.BooleanField(default=False, verbose_name='Помощь в организации')),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.systematicreport', verbose_name='Отчёт')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OneTimeParticipationApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=255, verbose_name='ФИО и должность лица, подтверждающего участие')),
                ('is_organizer', models.BooleanField(default=False, verbose_name='Организатор')),
                ('is_co_organizer', models.BooleanField(default=False, verbose_name='Соорганизатор')),
                ('is_assistant', models.BooleanField(default=False, verbose_name='Помощь в организации')),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.onetimeparticipationreport', verbose_name='Отчёт')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InformationSupportApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=255, verbose_name='ФИО и должность лица, подтверждающего участие')),
                ('scores', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Баллы')),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.informationsupportreport', verbose_name='Отчёт')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Баллы')),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.articlereport', verbose_name='Отчёт')),
            ],
        ),
    ]
