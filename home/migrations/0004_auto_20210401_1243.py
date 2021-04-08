# Generated by Django 3.1.7 on 2021-04-01 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210323_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='id',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default='Food', on_delete=django.db.models.deletion.SET_DEFAULT, to='home.categorie'),
        ),
    ]
