# Generated by Django 3.0.7 on 2022-06-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0003_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
