# Generated by Django 4.1.2 on 2022-11-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skil', '0005_remove_equestion_number_alter_equestion_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='equestion',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equestion',
            name='answer',
            field=models.IntegerField(),
        ),
    ]
