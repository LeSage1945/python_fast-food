# Generated by Django 4.0.10 on 2024-07-22 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_auteur_remove_produitbd_user_livre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='produitBD',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='date_publication',
        ),
        migrations.AlterField(
            model_name='auteur',
            name='nationalite',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='nom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='livre',
            name='auteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.auteur'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='titre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
