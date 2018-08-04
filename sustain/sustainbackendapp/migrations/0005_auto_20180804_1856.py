# Generated by Django 2.1 on 2018-08-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainbackendapp', '0004_auto_20180804_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=2),
        ),
    ]
