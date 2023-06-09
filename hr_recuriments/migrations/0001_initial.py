# Generated by Django 2.2 on 2022-11-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=40)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='imgs/')),
                ('education', models.CharField(max_length=1000)),
                ('skill', models.CharField(max_length=500)),
                ('experience', models.CharField(max_length=1000)),
                ('objective', models.CharField(max_length=500)),
                ('interest', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=15)),
            ],
        ),
    ]
