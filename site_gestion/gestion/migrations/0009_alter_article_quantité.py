# Generated by Django 4.1.6 on 2023-02-14 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_alter_article_quantité'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='quantité',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
