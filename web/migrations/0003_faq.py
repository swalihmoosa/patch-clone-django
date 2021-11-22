# Generated by Django 3.2.9 on 2021-11-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_promoter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('faq_type', models.CharField(choices=[('rent_tracking', 'Rent Tracking'), ('new_deposit', 'New Deposit'), ('existing_deposit', 'Existing Deposit')], max_length=255)),
            ],
        ),
    ]