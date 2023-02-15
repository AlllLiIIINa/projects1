from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models

from .validators import validate_start_date


class Group(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='name',
        db_column='name',
        validators=[MinLengthValidator(2, '"name" field value less than two symbols')]
    )
    description = models.TextField(
        max_length=500,
        verbose_name='description',
        db_column='description',
        validators=[MinLengthValidator(2, '"description" field value less than two symbols')]
    )
    start = models.DateField(default=date.today, null=True, blank=True, validators=[validate_start_date])

    def __str__(self):
        return f'{self.name} {self.description} {self.start}'

    class Meta:
        db_table = 'groups_table'
