# Generated by Django 4.2.14 on 2024-07-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebrand',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='phonebrand',
            unique_together={('name', 'nationality')},
        ),
    ]