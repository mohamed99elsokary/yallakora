# Generated by Django 4.0.4 on 2022-04-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicts', '0003_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchpredict',
            name='teamA_image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='matchpredict',
            name='teamB_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
