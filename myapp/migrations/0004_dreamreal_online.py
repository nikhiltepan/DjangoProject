# Generated by Django 2.2 on 2019-01-06 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='dreamreal',
            name='online',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.Online'),
        ),
    ]
