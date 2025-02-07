# Generated by Django 5.1.2 on 2024-10-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(default="desc"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="start_date",
            field=models.DateField(default="2024-10-10"),
            preserve_default=False,
        ),
    ]
