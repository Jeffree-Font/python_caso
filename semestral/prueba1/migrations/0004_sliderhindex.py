# Generated by Django 2.2.16 on 2020-10-31 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba1', '0003_auto_20201023_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderHindex',
            fields=[
                ('ident', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='autos')),
            ],
        ),
    ]
