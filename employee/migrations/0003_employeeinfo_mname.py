# Generated by Django 3.2.2 on 2021-06-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210616_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeinfo',
            name='mname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]