from django.core.exceptions import ValidationError # noqa
from django.utils.deconstruct import deconstructible # noqa

import students.models # noqa


# def valid_email_domains(value):
#     valid_domain = ['@gmail.com', '@yahoo.com']
#     for domain in valid_domain:
#         if domain in value:
#             break
#     else:
#         raise ValidationError(f'Email {value} has incorrect address.')
#
#
# def validate_unique_email(value):
#     valid_email = value
#     if students.models.Student.objects.filter(email=value).exists():
#         raise ValidationError(f'Email "{value}" already exists.')
#     return valid_email
#
#
# @deconstructible
# class ValidEmailDomain:
#     def __init__(self, *domains):
#         self.domains = list(domains)
#
#     def __call__(self, *args, **kwargs):
#         for domain in self.domains:
#             if args[0].endswith(domain):
#                 break
#         else:
#
#             raise ValidationError(f'Invalid email address. The domain [{args[0]}] not valid.')
