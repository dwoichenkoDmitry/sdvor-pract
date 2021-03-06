# Generated by Django 4.0.4 on 2022-07-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=20)),
                ('barcode', models.CharField(max_length=30)),
                ('codeType', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]
