from datetime import date

from django.core.exceptions import ValidationError

import groups.models


def validate_start_date(value):
    validate_start = str(value)
    today = str(date.today())
    if today <= validate_start:
        return validate_start
    else:
        raise ValidationError(f'start date "{value}" is earlier then now "{today}".')
