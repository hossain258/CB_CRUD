# Generated by Django 4.0.4 on 2022-05-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_studentdetails_student_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Description',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
