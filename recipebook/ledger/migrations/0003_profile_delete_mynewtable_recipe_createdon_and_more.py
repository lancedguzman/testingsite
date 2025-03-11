# Generated by Django 5.1.6 on 2025-03-10 05:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_rename_recipes_recipeingredient_recipe_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='', max_length=50)),
                ('bio', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MyNewTable',
        ),
        migrations.AddField(
            model_name='recipe',
            name='CreatedOn',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='UpdatedOn',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_author',
            field=models.CharField(default='', max_length=255),
        ),
    ]
