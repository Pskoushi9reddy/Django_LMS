# Generated by Django 5.0.6 on 2024-07-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_remove_student_first_name_remove_student_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
