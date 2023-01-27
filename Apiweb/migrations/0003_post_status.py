# Generated by Django 4.1.5 on 2023-01-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apiweb', '0002_post_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=30),
            preserve_default=False,
        ),
    ]
