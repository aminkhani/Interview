# Generated by Django 4.2.14 on 2024-07-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_remove_phonebrand_unique_name_nationality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]
