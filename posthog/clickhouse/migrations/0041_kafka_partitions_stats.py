from infi.clickhouse_orm import migrations

from posthog.models.kafka_partition_stats.sql import (
    CREATE_EVENTS_PLUGIN_INGESTION_PARTITION_STATISTICS_MV,
    CREATE_KAFKA_EVENTS_PLUGIN_INGESTION_PARTITION_STATISTICS,
    EVENTS_PLUGIN_INGESTION_PARTITION_STATISTICS,
)

operations = [
    migrations.RunSQL(CREATE_KAFKA_EVENTS_PLUGIN_INGESTION_PARTITION_STATISTICS()),
    migrations.RunSQL(EVENTS_PLUGIN_INGESTION_PARTITION_STATISTICS()),
    migrations.RunSQL(CREATE_EVENTS_PLUGIN_INGESTION_PARTITION_STATISTICS_MV()),
]