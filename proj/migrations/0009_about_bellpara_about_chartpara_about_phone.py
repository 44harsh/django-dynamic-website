# Generated by Django 4.1.1 on 2022-10-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0008_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='bellpara',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='chartpara',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]