# Generated by Django 4.1 on 2022-09-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bitiruvchi',
            field=models.BooleanField(default=False),
        ),
    ]
