# Generated by Django 4.1.3 on 2022-12-14 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prd_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.CharField(max_length=225)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='product/')),
                ('gender', models.CharField(max_length=225)),
                ('category', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='register_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('phonenumber', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='cart_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
                ('totalamount', models.CharField(max_length=225)),
                ('quantity', models.CharField(default='1', max_length=225)),
                ('status', models.CharField(default='pending', max_length=225)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app6.prd_tb')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app6.register_tb')),
            ],
        ),
    ]
