# Generated by Django 4.1.7 on 2023-08-15 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whyus',
            old_name='description_ar',
            new_name='why_majar_title_ar',
        ),
        migrations.RenameField(
            model_name='whyus',
            old_name='description_en',
            new_name='why_majar_title_en',
        ),
    ]
