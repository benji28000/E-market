# Generated by Django 4.1.6 on 2023-02-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0016_alter_panier_achat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='achat',
            field=models.ManyToManyField(to='gestion.achat'),
        ),
    ]
