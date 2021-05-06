from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Approvation(models.Model):
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, verbose_name='Дата оценивания')
    opinion_score = models.SmallIntegerField(verbose_name='Субъективная оценка')


class BaseReport(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    work = models.TextField(verbose_name='Выполненные работы по мероприятию')
    central_service_id = models.IntegerField(verbose_name='Id центрального сервиса')

    def __str__(self):
        return f'{self.title} report'


class BaseApp(models.Model):
    class Meta:
        abstract = True

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    responsible = models.CharField(max_length=255,
                                   verbose_name='ФИО и должность лица, подтверждающего участие')
    scores = models.PositiveSmallIntegerField(verbose_name='Баллы', null=True, blank=True)
    # approvation = models.ManyToManyField(Approvation, verbose_name='Проверено', blank=True)


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

    def __str__(self):
        return f'{self.report.title} app'


class ArticleReport(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    central_service_id = models.IntegerField(verbose_name='Id центрального сервиса')
    media_title = models.CharField(max_length=255, verbose_name='Название источника СМИ')
    EDITION_LEVEL = (
        ('university', 'университетский'),
        ('municipal', 'городской'),
    )
    edition_level_choicer = models.CharField(max_length=255, verbose_name='Уровень издания', choices=EDITION_LEVEL)
    co_author_quantity = models.PositiveSmallIntegerField(verbose_name='Количество соавторов', default=0)
    date = models.DateField(verbose_name='Дата публикации')


class ArticleApp(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.OneToOneField(ArticleReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    scores = models.PositiveSmallIntegerField(verbose_name='Баллы', null=True, blank=True)
