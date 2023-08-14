# Generated by Django 4.1.7 on 2023-08-14 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Why Us',
                'verbose_name_plural': 'Why Us',
            },
        ),
        migrations.CreateModel(
            name='WhyMajar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('icon', models.ImageField(upload_to='')),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Why Majar',
                'verbose_name_plural': 'Why Majar',
            },
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Vision',
                'verbose_name_plural': 'Vision',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Mission',
                'verbose_name_plural': 'Mission',
            },
        ),
        migrations.CreateModel(
            name='CustomHotline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_title_en', models.CharField(max_length=250)),
                ('sub_title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('custom_hotline_phone', models.PositiveIntegerField()),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Custom Hotline',
                'verbose_name_plural': 'Custom Hotline',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('title_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('icon', models.ImageField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('background', models.ImageField(upload_to='')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aboutus.header')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
    ]