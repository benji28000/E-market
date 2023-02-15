# Generated by Django 4.1.6 on 2023-02-14 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0014_achat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acheté_p', models.BooleanField(default=False)),
                ('date_achat', models.DateTimeField(blank=True, null=True)),
                ('achat', models.ManyToManyField(to='gestion.achat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]