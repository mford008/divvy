# Generated by Django 2.0.6 on 2018-06-30 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_sharegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
