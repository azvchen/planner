# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_section_section_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RequirementSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AddField(
            model_name='section',
            name='semester',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer')], default='Fall', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='year',
            field=models.IntegerField(default=2017),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_id',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='section',
            name='enrollment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('dept', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='instructor',
            unique_together=set([('name', 'dept')]),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('section_id', 'course', 'semester', 'year')]),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('requirementset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewer.RequirementSet')),
                ('degree_type', models.CharField(max_length=10)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.Department')),
            ],
            bases=('viewer.requirementset',),
        ),
        migrations.CreateModel(
            name='SchoolArea',
            fields=[
                ('requirementset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='viewer.RequirementSet')),
                ('school', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            bases=('viewer.requirementset',),
        ),
        migrations.AddField(
            model_name='courseset',
            name='courses',
            field=models.ManyToManyField(to='viewer.Course'),
        ),
        migrations.AddField(
            model_name='courseset',
            name='req_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.RequirementSet'),
        ),
        migrations.AlterUniqueTogether(
            name='degree',
            unique_together=set([('dept', 'degree_type')]),
        ),
    ]
