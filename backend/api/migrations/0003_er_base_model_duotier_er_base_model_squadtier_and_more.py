# Generated by Django 4.0.4 on 2022-04-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_er_base_model_averagedeal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='er_base_model',
            name='duoTier',
            field=models.CharField(default='Unrank', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='er_base_model',
            name='squadTier',
            field=models.CharField(default='Unrank', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='er_base_model',
            name='soloTier',
            field=models.CharField(default='Unrank', max_length=15, null=True),
        ),
    ]
