# Generated by Django 3.0.1 on 2019-12-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0019_order_user_extended'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cena_total_cart',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userextended',
            name='telefon',
            field=models.IntegerField(verbose_name='telefon'),
        ),
    ]
