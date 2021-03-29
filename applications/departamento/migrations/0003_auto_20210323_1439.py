# Generated by Django 3.1.7 on 2021-03-23 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210323_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mi departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]