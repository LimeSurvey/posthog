# Generated by Django 3.2.19 on 2023-12-07 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0372_cohort_query"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalDataSchema",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=400)),
                ("should_sync", models.BooleanField(default=True)),
                (
                    "latest_error",
                    models.TextField(help_text="The latest error that occurred when syncing this schema.", null=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemas",
                        to="posthog.externaldatasource",
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.datawarehousetable",
                    ),
                ),
                ("team", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.team")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]