# Generated by Django 2.2.1 on 2019-06-12 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descr', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('obs', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Categoria')),
            ],
        ),
    ]
