# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-06 04:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default='', max_length=2)),
                ('day', models.CharField(default='', max_length=2)),
                ('year', models.CharField(default='', max_length=4)),
                ('appttime', models.CharField(default='', max_length=5)),
                ('phase', models.CharField(default='', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('number', models.CharField(default='', max_length=13)),
                ('address', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LogInInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderName', models.CharField(default='', max_length=50)),
                ('senderType', models.CharField(default='', max_length=50)),
                ('receiverName', models.CharField(default='', max_length=50)),
                ('viewed', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date(2016, 12, 5))),
                ('subjectLine', models.CharField(default='', max_length=50)),
                ('message', models.TextField(default='', max_length=500)),
                ('senderDelete', models.BooleanField(default=False)),
                ('receiverDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=30)),
                ('workplace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('number', models.CharField(default='', max_length=13)),
                ('address', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('provider', models.CharField(default='', max_length=100)),
                ('insuranceid', models.CharField(default='', max_length=12)),
                ('height', models.CharField(default='', max_length=7)),
                ('weight', models.CharField(default='', max_length=6)),
                ('allergies', models.TextField(default='', max_length=500)),
                ('gender', models.CharField(default='', max_length=23)),
                ('username', models.CharField(default='', max_length=30)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.EmergencyContact')),
                ('hospital', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('dosage', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('released', models.BooleanField(default=False)),
                ('testResults', models.FileField(blank=True, null=True, upload_to='tests')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='workplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Patient'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='workplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Hospital'),
        ),
    ]
