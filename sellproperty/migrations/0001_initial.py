# Generated by Django 4.1.7 on 2023-08-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Phone', models.CharField(max_length=250)),
                ('Location', models.CharField(max_length=250)),
                ('Area', models.PositiveIntegerField()),
                ('Type', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Sell Property',
                'verbose_name_plural': 'Sell Property',
            },
        ),
    ]