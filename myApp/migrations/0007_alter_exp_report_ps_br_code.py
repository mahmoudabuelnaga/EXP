# Generated by Django 3.2 on 2021-04-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_auto_20210424_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exp_report',
            name='PS_BR_CODE',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
