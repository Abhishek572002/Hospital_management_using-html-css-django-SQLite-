# Generated by Django 4.0.6 on 2022-07-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0005_form1_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
