# Generated by Django 3.2.7 on 2022-02-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20220202_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='jobname',
            field=models.CharField(max_length=100, null='Job Prueba'),
        ),
    ]
