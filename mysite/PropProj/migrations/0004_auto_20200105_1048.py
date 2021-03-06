# Generated by Django 3.0.2 on 2020-01-05 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PropProj', '0003_remove_specs_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='specs',
            field=models.ManyToManyField(through='PropProj.DronePart', to='PropProj.Part'),
        ),
        migrations.AddField(
            model_name='part',
            name='specs',
            field=models.ManyToManyField(through='PropProj.PartSpecs', to='PropProj.Specs'),
        ),
        migrations.AddField(
            model_name='partspecs',
            name='value',
            field=models.CharField(default='heh', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dronepart',
            name='DroneID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PropProj.Drone'),
        ),
        migrations.AlterField(
            model_name='dronepart',
            name='PartID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PropProj.Part'),
        ),
        migrations.AlterField(
            model_name='partspecs',
            name='PartID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PropProj.Part'),
        ),
        migrations.AlterField(
            model_name='partspecs',
            name='SpecID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PropProj.Specs'),
        ),
    ]
