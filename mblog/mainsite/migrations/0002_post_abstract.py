# Generated by Django 2.2 on 2019-04-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
