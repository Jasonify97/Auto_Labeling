# Generated by Django 4.2.8 on 2024-01-19 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('classes_count', models.AutoField(primary_key=True, serialize=False)),
                ('classes_instance', models.CharField(max_length=100)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.userprofile')),
            ],
        ),
    ]