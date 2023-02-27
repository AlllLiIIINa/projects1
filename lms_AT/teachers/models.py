from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import ValidEmailDomain
from .validators import validate_unique_email


VALID_DOMAIN_LIST = ('gmail.com', 'yahoo.com')


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        db_column='first_name_c',
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        db_column='last_name_c',
        validators=[MinLengthValidator(2, '"last_name" field value less than two symbols')],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST), validate_unique_email])
    phone = models.CharField(
        max_length=100,
        verbose_name='phone number',
        db_column='phone_number_c',
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.pk} {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}@{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            phone = f.phone_number()
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email, phone=phone)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print(f'Incorrect data {first_name}, {last_name}, {birthday}, {email}, {phone}')
