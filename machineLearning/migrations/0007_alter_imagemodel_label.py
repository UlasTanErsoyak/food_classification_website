# Generated by Django 4.1.4 on 2023-01-19 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machineLearning', '0006_alter_imagemodel_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machineLearning.nutrition'),
        ),
    ]
