# Generated by Django 2.1.dev20180209010235 on 2018-02-27 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leasedetails',
            fields=[
                ('lease_id', models.AutoField(primary_key=True, serialize=False)),
                ('lease_start_date', models.DateField()),
                ('lease_end_date', models.DateField()),
                ('lease_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('tenant_id', models.AutoField(primary_key=True, serialize=False)),
                ('tenant_name', models.CharField(max_length=250)),
                ('tenant_company', models.CharField(max_length=250)),
                ('tenant_description', models.CharField(max_length=500)),
                ('tenant_joindate', models.DateField()),
                ('tenant_contact', models.IntegerField(unique=True)),
                ('tenant_secondry', models.IntegerField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='leasedetails',
            name='lease_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Room'),
        ),
        migrations.AddField(
            model_name='leasedetails',
            name='lease_tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Tenant'),
        ),
    ]
