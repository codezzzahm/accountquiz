# Generated by Django 3.2.4 on 2021-06-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ques', models.CharField(max_length=200)),
                ('choi1', models.CharField(max_length=20)),
                ('choi2', models.CharField(max_length=20)),
                ('ans', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
