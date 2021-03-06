# Generated by Django 3.2.3 on 2021-05-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pvgis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvgis',
            name='azimuth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pvgis',
            name='lat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pvgis',
            name='lon',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pvgis',
            name='loss',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pvgis',
            name='peakPower',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pvgis',
            name='slope',
            field=models.IntegerField(),
        ),
    ]
