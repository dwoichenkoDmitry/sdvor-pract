# Generated by Django 4.0.4 on 2022-07-11 18:14

from django.db import migrations
def create_data(apps, schema_editor):
    Documentes = apps.get_model('documentes', 'Documentes')
    Documentes(fileName="9999.jpg", number="6947586943", barcode="5869473859672", codeType="EAN13").save()

class Migration(migrations.Migration):

    dependencies = [
        ('documentes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]