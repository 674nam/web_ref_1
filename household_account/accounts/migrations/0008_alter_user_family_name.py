# Generated by Django 4.2.2 on 2024-03-27 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='family_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.family', verbose_name='家名'),
        ),
    ]
