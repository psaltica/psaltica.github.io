# Generated by Django 4.0 on 2022-01-08 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(editable=False, max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='translation',
            name='field',
            field=models.CharField(default='name', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='members',
            field=models.ManyToManyField(to='collection.Author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='author',
            name='lang',
            field=models.ForeignKey(default='ro', on_delete=django.db.models.deletion.PROTECT, to='collection.language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='translation',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.language'),
        ),
    ]