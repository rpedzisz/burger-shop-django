# Generated by Django 3.0.1 on 2019-12-25 02:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bar', '0016_auto_20191225_0301'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Cart',
        ),
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='CartItem',
        ),
    ]