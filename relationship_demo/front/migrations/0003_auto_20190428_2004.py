# Generated by Django 2.0.1 on 2019-04-28 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_userextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='front.FrontUser'),
        ),
    ]