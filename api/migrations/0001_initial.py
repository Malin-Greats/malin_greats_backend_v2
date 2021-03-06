# Generated by Django 3.2.7 on 2022-05-09 00:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgricultureDomain',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isOccupied', models.BooleanField(blank=True, default=False, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('companyName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='EducationDomain',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isOccupied', models.BooleanField(blank=True, default=False, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='HealthcareDomain',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isOccupied', models.BooleanField(blank=True, default=False, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturingDomain',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isOccupied', models.BooleanField(blank=True, default=False, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='RetailDomain',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('isOccupied', models.BooleanField(blank=True, default=False, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TotalDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('agricultureTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('retailTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('educationTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('manufacturingTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('healthcareTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TotalDomainQoutation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('agricultureTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('retailTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('educationTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('manufacturingTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('healthcareTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TotalSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('agricultureTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('retailTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('educationTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('manufacturingTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('healthcareTotal', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RetailSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.CharField(blank=True, default='Free', max_length=100, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.retaildomain')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ManufacturingSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.CharField(blank=True, default='Free', max_length=100, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.manufacturingdomain')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='HealthcareSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.CharField(blank=True, default='Free', max_length=100, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.healthcaredomain')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='EducationSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.CharField(blank=True, default='Free', max_length=100, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.educationdomain')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='AgricultureSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.CharField(blank=True, default='Free', max_length=100, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.agriculturedomain')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
