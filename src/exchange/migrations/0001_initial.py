# Generated by Django 2.1 on 2018-08-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('value', models.FloatField(max_length=15)),
                ('rate', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='rate.Rate')),
            ],
        ),
    ]
