# Generated by Django 2.1.5 on 2020-01-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20200122_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom'),
        ),
    ]