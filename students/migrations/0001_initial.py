# Generated by Django 5.1.2 on 2024-10-25 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_sch_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('suffix', models.CharField(blank=True, max_length=10)),
                ('birth_date', models.DateField()),
                ('country_of_birth', models.CharField(max_length=100)),
                ('birth_place', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('civil_status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced'), ('separated', 'Separated')], max_length=20)),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('religion', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('telephone_number', models.CharField(blank=True, max_length=20)),
                ('personal_email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', help_text="Student's account status", max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(blank=True, max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=20)),
                ('barangay', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]