# Generated by Django 5.0.6 on 2024-07-12 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_issuedbook_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=50),
        ),
    ]
