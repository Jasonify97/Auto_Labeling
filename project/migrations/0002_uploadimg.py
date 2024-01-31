# Generated by Django 4.2.9 on 2024-01-31 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_alter_userprofile_project_name'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='project')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.userprofile')),
            ],
        ),
    ]
