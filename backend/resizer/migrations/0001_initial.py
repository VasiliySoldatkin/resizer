# Generated by Django 3.1.6 on 2022-02-08 22:44

from django.db import migrations, models
import django.db.models.deletion
import resizer.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('url', models.URLField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, height_field='height', storage=resizer.storage.OverwriteStorage(), upload_to='resizer/%m/%d', verbose_name='picture', width_field='width')),
                ('height', models.PositiveSmallIntegerField(blank=True, editable=False, null=True)),
                ('width', models.PositiveSmallIntegerField(blank=True, editable=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('parent_picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resizer.imagesmodel')),
            ],
        ),
    ]
