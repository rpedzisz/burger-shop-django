# Generated by Django 3.0.1 on 2019-12-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0014_orderitem_cena_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='obraz',
            field=models.IntegerField(default=1, verbose_name='obraz'),
            preserve_default=False,
        ),
    ]
