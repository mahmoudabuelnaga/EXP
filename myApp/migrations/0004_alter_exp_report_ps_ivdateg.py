# Generated by Django 3.2 on 2021-04-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20210424_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exp_report',
            name='PS_IVDATEG',
            field=models.DateField(blank=True, null=True),
        ),
    ]
