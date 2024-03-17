# Generated by Django 4.2.2 on 2024-02-15 04:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('mail', models.EmailField(max_length=100)),
            ],
        ),
    ]