# Generated by Django 2.1.5 on 2019-01-26 14:16

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
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('semester', models.PositiveIntegerField(default=1)),
                ('author', models.CharField(max_length=200)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('is_assigned', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]