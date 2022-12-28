# Generated by Django 4.1.3 on 2022-12-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contactNumber', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]