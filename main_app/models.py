from django.db import models


class OneTimeParticipationReport(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    work = models.TextField(verbose_name='Выполненные работы по мероприятию')
    # date = models.DateField(verbose_name='Дата мероприятия')


class OneTimeParticipationApp(models.Model):
    report = models.OneToOneField(OneTimeParticipationReport, verbose_name='Отчёт', on_delete=models.CASCADE)
    responsible = models.CharField(max_length=255, verbose_name='ФИО и должность лица, подтверждающего участие')  # В лучшем случае foreignkey, ссылающийся на дядю или тетю
    is_organizer = models.BooleanField(verbose_name='Организатор', default=False)
    is_co_organizer = models.BooleanField(verbose_name='Соорганизатор', default=False)
    is_assistant = models.BooleanField(verbose_name='Помощь в организации', default=False)

    def save(self, *args, **kwargs):
        error = int(self.is_organizer) + int(self.is_co_organizer) + int(self.is_assistant)
        if error != 1:
            raise ValueError('test exception')
        super().save(*args, **kwargs)


class Application(models.Model):
    # owner= models.ForeignKey
    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    work = models.TextField(verbose_name='Выполненные работы по мероприятию')
    start_date = models.DateField(verbose_name='Дата начала мероприятия')
    finish_date = models.DateField(verbose_name='Дата конца мероприятия')
    responsible = models.CharField(max_length=255,
                                   verbose_name='ФИО и должность лица, подтверждающего участие')  # В лучшем случае foreignkey, ссылающийся на дядю или тетю
    is_organizer = models.BooleanField(verbose_name='Организатор', default=False)
    is_co_organizer = models.BooleanField(verbose_name='Соорганизатор', default=False)
    is_assistant = models.BooleanField(verbose_name='Помощь в организации', default=False)

    def save(self, *args, **kwargs):
        error = int(self.is_organizer) + int(self.is_co_organizer) + int(self.is_assistant)
        if error != 1:
            raise ValueError('test exception')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    work = models.TextField(verbose_name='Выполненные работы по мероприятию')
    start_date = models.DateField(verbose_name='Дата начала мероприятия')
    finish_date = models.DateField(verbose_name='Дата конца мероприятия')
    is_systematic = models.BooleanField(verbose_name='Систематична')

    TYPE_CHOICER = (
        ('volunteer', 'Волонтёр'),
        ('info_support', 'Информационное обеспечение'),
        ('other', 'Другое'),
    )

    type = models.CharField(max_length=31, verbose_name='Тип систематической деятельности', choices=TYPE_CHOICER,
                            blank=True, null=True, default='other')

    def save(self, *args, **kwargs):
        if not self.is_systematic:
            self.type = None
        super().save(*args, **kwargs)
