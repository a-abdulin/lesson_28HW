# Generated by Django 4.1.7 on 2023-02-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
