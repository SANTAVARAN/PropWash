# Generated by Django 3.0.2 on 2020-01-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ESC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoltageRate', models.CharField(max_length=20)),
                ('CurrentRate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoltageRate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagonal', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Motors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoltageRate', models.CharField(max_length=20)),
                ('MaxCurrent', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AntennaType', models.CharField(max_length=20)),
                ('Connector', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VoltageRate', models.CharField(max_length=20)),
                ('Protocol', models.CharField(max_length=20)),
            ],
        ),
    ]