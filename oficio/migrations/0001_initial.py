# Generated by Django 3.2.16 on 2022-10-09 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paragrafo1', '0001_initial'),
        ('rodape', '0001_initial'),
        ('paragrafo2', '0001_initial'),
        ('cabecalho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabecalho', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cabecalho', to='cabecalho.cabecalho')),
                ('paragrafo1', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='paragrafo1', to='paragrafo1.paragrafo1')),
                ('paragrafo2', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='paragrafo2', to='paragrafo2.paragrafo2')),
                ('rodape', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rodape', to='rodape.rodape')),
            ],
        ),
    ]