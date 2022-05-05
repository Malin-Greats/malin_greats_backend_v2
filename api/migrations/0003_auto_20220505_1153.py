# Generated by Django 3.2.7 on 2022-05-05 11:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_healthcaresignup_manufacturingsignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='agriculturesignup',
            name='account',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='AgricultureDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isOccupied', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.agriculturesignup')),
            ],
        ),
    ]