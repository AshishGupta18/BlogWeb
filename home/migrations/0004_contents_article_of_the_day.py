# Generated by Django 4.2.3 on 2023-11-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_msgfromadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='article_of_the_day',
            field=models.BooleanField(default=False),
        ),
    ]
