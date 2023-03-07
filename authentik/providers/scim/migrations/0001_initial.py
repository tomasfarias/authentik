# Generated by Django 4.1.7 on 2023-03-02 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_core", "0024_source_icon"),
    ]

    operations = [
        migrations.CreateModel(
            name="SCIMMapping",
            fields=[
                (
                    "propertymapping_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_core.propertymapping",
                    ),
                ),
            ],
            options={
                "verbose_name": "SCIM Mapping",
                "verbose_name_plural": "SCIM Mappings",
            },
            bases=("authentik_core.propertymapping",),
        ),
        migrations.CreateModel(
            name="SCIMProvider",
            fields=[
                (
                    "provider_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_core.provider",
                    ),
                ),
                (
                    "url",
                    models.TextField(help_text="Base URL to SCIM requests, usually ends in /v2"),
                ),
                ("token", models.TextField(help_text="Authentication token")),
            ],
            options={
                "verbose_name": "SCIM Provider",
                "verbose_name_plural": "SCIM Providers",
            },
            bases=("authentik_core.provider",),
        ),
    ]