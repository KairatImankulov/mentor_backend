# Generated by Django 4.2.4 on 2023-09-04 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_category_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='announcement.subcategory'),
        ),
    ]
