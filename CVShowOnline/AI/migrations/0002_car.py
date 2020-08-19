# Generated by Django 3.0.5 on 2020-08-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(upload_to='cars')),
            ],
        ),
    ]
