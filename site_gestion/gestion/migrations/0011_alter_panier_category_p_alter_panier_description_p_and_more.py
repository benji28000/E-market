# Generated by Django 4.1.6 on 2023-02-14 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_panier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='category_p',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.category'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='description_p',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='panier',
            name='title_p',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
