import random

from django.db import models


class UUIDGenerator:
    """Генерирует и проверяет uuid.
    """
    def __init__(self, obj):
        """
        Args:
            obj (_type_):
                Объект для которого будет сгенерирован uuid.
        Vars:
            obj (_type_): Объект.
            pk (str): id объекта.
            date (str): Дата создания объекта.
            body (str): Текст объекта.
        """
        self.obj = obj
        self.pk = str(obj.pk)
        self.date = str(obj.created)
        self.body = str(obj.body)

    def create_uuid(self):
        """Составляет uuid из полей объекта.

        Returns:
            uuid (str): uuid.
        """
        uuid = ''.join(
            ch for ch in random.sample(
                f'{self.body}{self.pk}{self.date}',
                8
            )
            if ch != ' '
        )
        return uuid

    def generate_uuid(self):
        """Генерирует uuid до того момента пока он не станет уникальным среди
        всех обЪектов.

        Returns:
            uuid(str): uuid.
        """
        uuid = self.create_uuid()
        records = type(self.obj).objects.all().values_list('uuid', flat=True)
        while uuid in records:
            uuid = self.create_uuid()
        return uuid


class Record(models.Model):
    uuid = models.CharField(
        max_length=8,
        unique=True,
        verbose_name='Уникальная строка идентификатор'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    body = models.TextField(
        max_length=2000,
        verbose_name='Текст записи'
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Статус записи'
    )

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)
        rec = type(self).objects.filter(pk=self.id)
        rec.update(uuid=UUIDGenerator(self).generate_uuid())

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
