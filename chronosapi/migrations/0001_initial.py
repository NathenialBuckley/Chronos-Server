# Generated by Django 4.1.3 on 2023-01-09 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=155)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postalCode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('image', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=300)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronosapi.customer')),
                ('watchtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watches', to='chronosapi.watchtype')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('price', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronosapi.customer')),
                ('watchtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_watches', to='chronosapi.watchtype')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronosapi.customer')),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronosapi.watch')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronosapi.customer')),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronosapi.watch')),
            ],
        ),
    ]
