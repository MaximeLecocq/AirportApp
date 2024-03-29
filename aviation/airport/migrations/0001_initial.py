# Generated by Django 5.0 on 2023-12-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id of airport')),
                ('airport_name', models.CharField(max_length=100, verbose_name='name of airport')),
                ('airport_type', models.CharField(choices=[('LARGE', 'large airport'), ('MEDIUM', 'medium airport'), ('SMALL', 'small airport'), ('SEAPLANE', 'seaplane base'), ('HELIPORT', 'heliport')], max_length=25, verbose_name='type of airport')),
                ('latitude', models.FloatField(verbose_name='latitude degree')),
                ('longitude', models.FloatField(verbose_name='longitude degree')),
                ('elevation', models.IntegerField(blank=True, null=True, verbose_name='elevation')),
                ('continent', models.CharField(choices=[('ASIA', 'Asia'), ('SOUTH_AND_CENTRAL_AMERICA', 'South and Central America'), ('OCEANIA', 'Oceania'), ('AFRICA', 'Africa'), ('EUROPE', 'Europe'), ('NORTH_AMERICA', 'North America'), ('ANTARTICA', 'Antartica')], max_length=40, verbose_name='continent')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
                ('municipality', models.CharField(blank=True, max_length=100, null=True, verbose_name='municipality')),
            ],
            options={
                'ordering': ['airport_id', 'airport_name', 'airport_type', 'latitude', 'longitude', 'elevation', 'continent', 'country', 'municipality'],
            },
        ),
    ]
