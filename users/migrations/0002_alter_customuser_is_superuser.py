# Generated by Django 4.1.1 on 2023-02-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Indica que este usuario tiene todos los permisos', verbose_name='Es administrador'),
        ),
    ]
