import datetime
import django.core.validators
from django.db import migrations, models
import teachers.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name_c', max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"first_name" field value less than two symbols')], verbose_name='first name')),
                ('last_name', models.CharField(db_column='last_name_c', error_messages={'min_length': '"last_name" field value less than two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"last_name" field value less than two symbols')], verbose_name='last name')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('email', models.EmailField(max_length=254, validators=[teachers.validators.ValidEmailDomain('gmail.com', 'yahoo.com'), teachers.validators.validate_unique_email])),
                ('phone', models.CharField(blank=True, db_column='phone_number_c', max_length=100, null=True, verbose_name='phone number')),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]
