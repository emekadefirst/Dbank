# Generated by Django 4.2.3 on 2023-08-19 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customuser_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
