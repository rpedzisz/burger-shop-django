# Generated by Django 3.0.1 on 2019-12-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0006_auto_20191224_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skladnik',
            name='burger',
        ),
        migrations.AddField(
            model_name='burger',
            name='skladniki',
            field=models.ManyToManyField(to='bar.Skladnik'),
        ),
    ]
