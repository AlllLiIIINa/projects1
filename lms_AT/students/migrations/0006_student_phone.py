# Generated by Django 4.1.7 on 2023-02-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, db_column='phone_number_c', max_length=100, null=True, verbose_name='phone number'),
        ),
    ]
