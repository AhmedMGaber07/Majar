# Generated by Django 4.1.7 on 2023-08-13 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Call',
                'verbose_name_plural': 'Call',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='DeliveryConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Delivery Conditions',
                'verbose_name_plural': 'Delivery Conditions',
            },
        ),
        migrations.CreateModel(
            name='DeliveryTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
                ('year', models.DateField()),
            ],
            options={
                'verbose_name': 'Delivery Types',
                'verbose_name_plural': 'Delivery Types',
            },
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Developers',
                'verbose_name_plural': 'Developers',
            },
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=250)),
                ('name_ar', models.CharField(blank=True, max_length=250, null=True)),
                ('bedroom_number', models.PositiveIntegerField()),
                ('bathroom_number', models.PositiveIntegerField()),
                ('move_now_pay_later', models.BooleanField(default=False)),
                ('area', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('description_en', models.TextField(max_length=500)),
                ('description_ar', models.TextField(blank=True, max_length=500, null=True)),
                ('floor_plan', models.URLField()),
                ('master_plan', models.URLField()),
                ('location_link', models.TextField(max_length=500)),
                ('show_in_home_page', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Properties',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Locations',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Developers',
                'verbose_name_plural': 'Developers',
            },
        ),
        migrations.CreateModel(
            name='PropertySubTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=254)),
                ('name_ar', models.CharField(blank=True, max_length=254, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.propertytypes')),
            ],
            options={
                'verbose_name': 'Developers',
                'verbose_name_plural': 'Developers',
            },
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=False)),
                ('Properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.general')),
            ],
            options={
                'verbose_name': 'Property Images',
                'verbose_name_plural': 'Property Images',
            },
        ),
        migrations.CreateModel(
            name='PopularLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.locations')),
            ],
            options={
                'verbose_name': 'Popular Locations',
                'verbose_name_plural': 'Popular Locations',
            },
        ),
        migrations.CreateModel(
            name='PopularDevelopers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.developers')),
            ],
            options={
                'verbose_name': 'Popular Developers',
                'verbose_name_plural': 'Popular Developers',
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('down_price', models.PositiveIntegerField()),
                ('monthly_instalments', models.PositiveIntegerField()),
                ('instalment_years', models.PositiveIntegerField()),
                ('delivery_payment', models.PositiveIntegerField()),
                ('Properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.general')),
            ],
            options={
                'verbose_name': 'Plans',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.AddField(
            model_name='general',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.propertysubtypes'),
        ),
        migrations.AddField(
            model_name='general',
            name='call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.call'),
        ),
        migrations.AddField(
            model_name='general',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.category'),
        ),
        migrations.AddField(
            model_name='general',
            name='delivery_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.deliveryconditions'),
        ),
        migrations.AddField(
            model_name='general',
            name='delivery_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.deliverytypes'),
        ),
        migrations.AddField(
            model_name='general',
            name='developed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.populardevelopers'),
        ),
        migrations.AddField(
            model_name='general',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.popularlocations'),
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubhouse', models.BooleanField(default=False)),
                ('schools', models.BooleanField(default=False)),
                ('medical_center', models.BooleanField(default=False)),
                ('commercial_strip', models.BooleanField(default=False)),
                ('business_hub', models.BooleanField(default=False)),
                ('sports_clubs', models.BooleanField(default=False)),
                ('bicycles_lanes', models.BooleanField(default=False)),
                ('jogging_trail', models.BooleanField(default=False)),
                ('Properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.general')),
            ],
            options={
                'verbose_name': 'Amenities',
                'verbose_name_plural': 'Amenities',
            },
        ),
    ]
