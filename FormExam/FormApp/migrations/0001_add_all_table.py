# Generated by Django 4.1 on 2024-03-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('picture', models.FileField(upload_to='')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FormApp.class')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
