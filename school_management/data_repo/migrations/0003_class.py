# Generated by Django 3.1.5 on 2021-01-25 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_repo', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.IntegerField(unique=True)),
                ('section', models.CharField(max_length=255)),
                ('room_no', models.IntegerField(unique=True)),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_repo.teacher')),
            ],
        ),
    ]
