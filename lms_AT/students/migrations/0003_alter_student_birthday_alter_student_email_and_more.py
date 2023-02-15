# Generated by Django 4.1.1 on 2023-02-14 16:47

import datetime
from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_email_alter_student_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, validators=[students.validators.ValidEmailDomain('@gmail.com', '@yahoo.com')]),
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
