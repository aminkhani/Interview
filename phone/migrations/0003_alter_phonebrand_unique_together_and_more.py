# Generated by Django 4.2.14 on 2024-07-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_alter_phonebrand_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='phonebrand',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='phonebrand',
            constraint=models.UniqueConstraint(fields=('name', 'nationality'), name='unique_name_nationality'),
        ),
    ]