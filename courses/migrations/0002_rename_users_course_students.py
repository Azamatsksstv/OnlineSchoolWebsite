# Generated by Django 4.2.3 on 2023-07-12 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='users',
            new_name='students',
        ),
    ]