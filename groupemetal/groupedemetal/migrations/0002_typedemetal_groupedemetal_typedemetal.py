# Generated by Django 4.0.4 on 2022-05-13 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groupedemetal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typedemetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registre', models.CharField(max_length=100)),
                ('sous_registre', models.CharField(max_length=100)),
                ('resume', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='groupedemetal',
            name='typedemetal',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='groupedemetal.typedemetal'),
        ),
    ]
