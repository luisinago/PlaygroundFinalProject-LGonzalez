# Generated by Django 4.2.6 on 2023-11-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sailor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=10)),
                ('planeta', models.CharField(max_length=50)),
                ('objeto', models.CharField(max_length=20)),
            ],
        ),
    ]
