# Generated by Django 2.0.1 on 2018-01-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdocuments',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
