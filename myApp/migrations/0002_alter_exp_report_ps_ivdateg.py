# Generated by Django 3.2 on 2021-04-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exp_report',
            name='PS_IVDATEG',
            field=models.DateField(),
        ),
    ]
