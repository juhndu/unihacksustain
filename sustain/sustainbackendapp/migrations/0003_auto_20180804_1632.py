# Generated by Django 2.1 on 2018-08-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainbackendapp', '0002_auto_20180804_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='restaurant',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(verbose_name=0),
        ),
    ]