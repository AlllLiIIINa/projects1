from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import students.models


def valid_email_domains(value):
    valid_domain = ['@gmail.com', '@yahoo.com']
    for domain in valid_domain:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email {value} has incorrect address.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:

            raise ValidationError(f'Invalid email address. The domain {args[0].split("@")} not valid.')
