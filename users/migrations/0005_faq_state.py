# Generated by Django 3.2 on 2022-05-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='state',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]