# Generated by Django 3.2.16 on 2022-10-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0003_auto_20221014_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficio',
            name='cabecalho',
        ),
        migrations.AddField(
            model_name='oficio',
            name='cabecalho',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
