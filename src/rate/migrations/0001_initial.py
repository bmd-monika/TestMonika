# Generated by Django 2.1 on 2018-08-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fromRate', models.CharField(blank=True, default='', max_length=100)),
                ('toRate', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
