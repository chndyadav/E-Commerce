# Generated by Django 3.0.5 on 2020-06-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('public_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
