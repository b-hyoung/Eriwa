# Generated by Django 4.0.4 on 2022-05-09 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_averagerank_er_user_info_model_averageranking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='er_stats_model',
            old_name='averageRank',
            new_name='averageRanking',
        ),
    ]
