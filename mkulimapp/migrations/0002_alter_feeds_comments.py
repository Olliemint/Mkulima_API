# Generated by Django 4.0.5 on 2022-06-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkulimapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='farmer_post', to='mkulimapp.comment'),
        ),
    ]
