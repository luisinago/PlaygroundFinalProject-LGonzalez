# Generated by Django 4.2.6 on 2023-11-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personajes', '0002_winx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Witch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=10)),
                ('elemento', models.CharField(max_length=50)),
                ('signo', models.CharField(max_length=20)),
            ],
        ),
    ]
