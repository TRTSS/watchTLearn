# Generated by Django 4.1.6 on 2023-02-10 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('users', '0003_customuser_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='userRole',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roles.role'),
        ),
    ]
