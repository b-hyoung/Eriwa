# Generated by Django 4.0.4 on 2022-05-09 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charName', models.CharField(max_length=30, null=True)),
                ('Weapon', models.IntegerField(null=True)),
                ('Haed', models.IntegerField(null=True)),
                ('Clothes', models.IntegerField(null=True)),
                ('Arm', models.IntegerField(null=True)),
                ('Leg', models.IntegerField(null=True)),
                ('Accessories', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MasteryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('mmr', models.IntegerField(default=0, null=True)),
                ('averagebestWeaponLevel', models.IntegerField(null=True)),
                ('averageTraplevel', models.IntegerField(null=True)),
                ('averageProductionlevel', models.IntegerField(null=True)),
                ('averageSearchlevel', models.IntegerField(null=True)),
                ('averageMovelevel', models.IntegerField(null=True)),
                ('averageStrengthlevel', models.IntegerField(null=True)),
                ('averageDefenselevel', models.IntegerField(null=True)),
                ('averageHuntinglevel', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MostPickModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('matchingTeamMode', models.CharField(max_length=10)),
                ('season', models.CharField(default=0, max_length=10, null=True)),
                ('most_one_charName', models.CharField(max_length=30, null=True)),
                ('most_one_charImage', models.ImageField(null=True, upload_to='')),
                ('most_one_averageRank', models.IntegerField(null=True)),
                ('most_two_char', models.IntegerField(null=True)),
                ('most_two_averageRank', models.IntegerField(null=True)),
                ('most_three_char', models.IntegerField(null=True)),
                ('most_three_averageRank', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TraitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstCore', models.IntegerField(null=True)),
                ('FirstSub_one', models.IntegerField(null=True)),
                ('FirstSub_two', models.IntegerField(null=True)),
                ('SecondSub_one', models.IntegerField(null=True)),
                ('SecondSub_two', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ER_User_Info_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('userNum', models.CharField(max_length=20)),
                ('mmr', models.IntegerField(default=0, null=True)),
                ('soloTier', models.CharField(default='Unrank', max_length=15, null=True)),
                ('duoTier', models.CharField(default='Unrank', max_length=15, null=True)),
                ('squadTier', models.CharField(default='Unrank', max_length=15, null=True)),
                ('averageRank', models.FloatField(null=True)),
                ('averageKills', models.FloatField(null=True)),
                ('averageHunts', models.FloatField(null=True)),
                ('averageDeal', models.FloatField(null=True)),
                ('averageProficiency', models.FloatField(null=True)),
                ('averageAssistants', models.FloatField(default=0, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mastery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mastery', to='api.masterymodel')),
                ('mostpick', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mostpick', to='api.mostpickmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ER_Stats_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=30, null=True)),
                ('matchingMode', models.CharField(max_length=10)),
                ('matchingTeamMode', models.CharField(max_length=10)),
                ('season', models.CharField(default=0, max_length=10)),
                ('character', models.CharField(max_length=50)),
                ('lavel', models.IntegerField(default=1)),
                ('bestWeapon', models.CharField(max_length=30)),
                ('averageRank', models.FloatField(default=9)),
                ('averageKills', models.FloatField(null=True)),
                ('averageHunts', models.FloatField(null=True)),
                ('averageDeal', models.FloatField(null=True)),
                ('averageProficiency', models.FloatField(null=True)),
                ('averageAssistants', models.FloatField(null=True)),
                ('averageItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.itemmodel')),
                ('averageTrait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.traitmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ER_Game_Record_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('season', models.CharField(default=0, max_length=10)),
                ('ranking', models.IntegerField()),
                ('matchingMode', models.CharField(max_length=10)),
                ('matchingTeamMode', models.CharField(max_length=10)),
                ('character', models.CharField(max_length=50)),
                ('characterlevel', models.IntegerField(default=1)),
                ('bestWeapon', models.CharField(max_length=30)),
                ('bestWeaponLevel', models.IntegerField(default=1)),
                ('Kills', models.FloatField(null=True)),
                ('Hunts', models.FloatField(null=True)),
                ('Assistants', models.FloatField(null=True)),
                ('mmr', models.IntegerField(default=0, null=True)),
                ('Route', models.IntegerField(default=0, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.traitmodel')),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.itemmodel')),
            ],
        ),
    ]
