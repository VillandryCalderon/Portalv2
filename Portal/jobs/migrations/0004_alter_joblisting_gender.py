# Generated by Django 3.2.7 on 2022-01-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_joblisting_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], max_length=30, null=True),
        ),
    ]
