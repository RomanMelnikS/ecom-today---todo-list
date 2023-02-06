import random

from django.db import models


class UUIDGenerator:
    def __init__(self, obj):
        self.obj = obj
        self.pk = str(obj.pk)
        self.date = str(obj.created)
        self.body = str(obj.body)

    def generate_uuid(self):
        uuid = ''.join(
            ch for ch in random.sample(
                f'{self.body}{self.pk}{self.date}',
                8
            )
            if ch != ' '
        )
        return uuid

    def chek_uuid(self):
        uuid = self.generate_uuid()
        records = type(self.obj).objects.all().values_list('uuid', flat=True)
        while uuid in records:
            uuid = self.generate_uuid()
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
        rec.update(uuid=UUIDGenerator(self).chek_uuid())

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
