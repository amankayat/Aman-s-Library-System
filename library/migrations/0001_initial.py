# Generated by Django 4.0.3 on 2022-06-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publish', models.DateField()),
            ],
        ),
    ]