# Generated by Django 2.0.1 on 2018-02-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20180122_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdocuments',
            name='uploaded_file',
            field=models.FileField(null=True, upload_to='upload_documents'),
        ),
    ]
