# Generated by Django 3.0.1 on 2019-12-23 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skladnik',
            name='burger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skladniki', to='bar.Burger'),
        ),
        migrations.CreateModel(
            name='ZamowienieObiekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czy_zamowione', models.BooleanField(default=False)),
                ('produkt', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bar.Burger')),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produkty', models.ManyToManyField(to='bar.ZamowienieObiekt')),
            ],
        ),
    ]