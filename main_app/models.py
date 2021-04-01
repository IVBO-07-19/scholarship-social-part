from django.db import models


class BaseReport(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    work = models.TextField(verbose_name='Выполненные работы по мероприятию')

    def __str__(self):
        return f'{self.title} report'


class BaseApp(models.Model):
    class Meta:
        abstract = True

    # owner=User
    # responsible=User
    responsible = models.CharField(max_length=255,
                                   verbose_name='ФИО и должность лица, подтверждающего участие')  # В лучшем случае foreignkey, ссылающийся на дядю или тетю


class OneTimeParticipationReport(BaseReport):
    date = models.DateField(verbose_name='Даты проведения')


class OneTimeParticipationApp(BaseApp):
    report = models.OneToOneField(OneTimeParticipationReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    is_organizer = models.BooleanField(verbose_name='Организатор', default=False)
    is_co_organizer = models.BooleanField(verbose_name='Соорганизатор', default=False)
    is_assistant = models.BooleanField(verbose_name='Помощь в организации', default=False)

    def __str__(self):
        return f'{self.report.title} app'

    def save(self, *args, **kwargs):
        error = int(self.is_organizer) + int(self.is_co_organizer) + int(self.is_assistant)
        if error != 1:
            raise ValueError('test exception')
        super().save(*args, **kwargs)


class SystematicReport(BaseReport):
    start_date = models.DateField(verbose_name='Начало выполнения деятельности')
    final_date = models.DateField(verbose_name='Конец выполнения деятельности')


class SystematicApp(BaseApp):
    report = models.OneToOneField(SystematicReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    is_organizer = models.BooleanField(verbose_name='Организатор', default=False)
    is_co_organizer = models.BooleanField(verbose_name='Соорганизатор', default=False)
    is_assistant = models.BooleanField(verbose_name='Помощь в организации', default=False)

    def __str__(self):
        return f'{self.report.title} app'

    def save(self, *args, **kwargs):
        error = int(self.is_organizer) + int(self.is_co_organizer) + int(self.is_assistant)
        if error != 1:
            raise ValueError('test exception')
        super().save(*args, **kwargs)


class VolunteerReport(BaseReport):
    date = models.DateField(verbose_name='Даты проведения')


class VolunteerApp(BaseApp):
    report = models.OneToOneField(VolunteerReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    is_leader = models.BooleanField(verbose_name='Руководитель', default=False)
    is_organizer = models.BooleanField(verbose_name='Организатор', default=False)
    is_teamleader = models.BooleanField(verbose_name='Тимлидер', default=False)
    is_volunteer = models.BooleanField(verbose_name='Волонтёр', default=False)

    def __str__(self):
        return f'{self.report.title} app'

    def save(self, *args, **kwargs):
        error = int(self.is_organizer) + int(self.is_leader) + int(self.is_teamleader) + int(self.is_volunteer)
        if error != 1:
            raise ValueError('test exception')
        super().save(*args, **kwargs)


class InformationSupportReport(BaseReport):
    start_date = models.DateField(verbose_name='Начало выполнения деятельности')
    final_date = models.DateField(verbose_name='Конец выполнения деятельности')


class InformationSupportApp(BaseApp):
    report = models.OneToOneField(InformationSupportReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    scores = models.PositiveSmallIntegerField(verbose_name='Баллы', null=True, blank=True)

    def __str__(self):
        return f'{self.report.title} app'


class ArticleReport(models.Model):
    # owner=User
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    media_title = models.CharField(max_length=255, verbose_name='Название источника СМИ')
    EDITION_LEVEL = (
        ('university', 'университетский'),
        ('municipal', 'городской'),
    )
    edition_level_choicer = models.CharField(max_length=255, verbose_name='Уровень издания', choices=EDITION_LEVEL)
    co_author_quantity = models.PositiveSmallIntegerField(verbose_name='Количество соавторов', default=0)
    date = models.DateField(verbose_name='Дата публикации')


class ArticleApp(models.Model):
    report = models.OneToOneField(ArticleReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    scores = models.PositiveSmallIntegerField(verbose_name='Баллы', null=True, blank=True)
