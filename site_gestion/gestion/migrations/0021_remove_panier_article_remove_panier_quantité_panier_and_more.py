# Generated by Django 4.1.6 on 2023-02-14 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0020_remove_panier_achat_remove_panier_acheté_p_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='article',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='quantité_panier',
        ),
        migrations.AddField(
            model_name='panier',
            name='acheté_p',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantité_achat', models.IntegerField(default=1)),
                ('acheté', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='panier',
            name='achat',
            field=models.ManyToManyField(to='gestion.achat'),
        ),
    ]
