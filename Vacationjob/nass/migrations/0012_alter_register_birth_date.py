# Generated by Django 5.1.4 on 2024-12-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nass', '0011_alter_register_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]