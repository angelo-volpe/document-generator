# Generated by Django 5.1.2 on 2024-11-01 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentapp', '0003_document_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxCoordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.IntegerField()),
                ('y1', models.IntegerField()),
                ('x2', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box_coordinates', to='documentapp.document')),
            ],
        ),
    ]