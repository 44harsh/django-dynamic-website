# Generated by Django 4.1.1 on 2022-10-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0011_acceptemp'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptemp',
            name='status',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='empsignup',
            name='status',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
